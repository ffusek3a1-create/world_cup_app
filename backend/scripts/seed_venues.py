"""
seed_venues.py
--------------
Seeds the 'venues' table in world_cup.db from data_venues.py.
Also updates the 'matches' table so each row references its venue_id
(requires the matches table to already exist from seed_schedule.py).

Schema added:
  venues
    id          INTEGER PK
    name        VARCHAR  (commercial name)
    fifa_name   VARCHAR  (official FIFA tournament name)
    city        VARCHAR
    state       VARCHAR
    country     VARCHAR
    capacity    INTEGER
    matches     INTEGER  (total matches hosted)
    roof        VARCHAR
    nfl_tenant  VARCHAR
    opened      INTEGER  (year)
    region      VARCHAR  (Western / Central / Eastern)
    lat         REAL
    lon         REAL
    notes       VARCHAR

  matches table gets a new column:
    venue_id    INTEGER  (FK → venues.id)

Run from the backend/ directory:
    python scripts/seed_venues.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_venues import VENUES

from sqlalchemy import (
    Column, Integer, String, Float, text,
    create_engine, inspect
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os as _os
_DB_PATH = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "world_cup.db")
DATABASE_URL = "sqlite:///" + _DB_PATH
engine  = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
Base    = declarative_base()


class Venue(Base):
    __tablename__ = "venues"
    id         = Column(Integer, primary_key=True, index=True)
    name       = Column(String, unique=True)
    fifa_name  = Column(String)
    city       = Column(String)
    state      = Column(String)
    country    = Column(String)
    capacity   = Column(Integer)
    matches    = Column(Integer)
    roof       = Column(String)
    nfl_tenant = Column(String)
    opened     = Column(Integer)
    region     = Column(String)
    lat        = Column(Float)
    lon        = Column(Float)
    notes      = Column(String)


def add_column_if_missing(conn, table, column, col_type):
    existing = [c["name"] for c in inspect(engine).get_columns(table)]
    if column not in existing:
        conn.execute(text(f"ALTER TABLE {table} ADD COLUMN {column} {col_type}"))
        print(f"  + Added column '{column}' to '{table}'.")


def seed():
    Base.metadata.create_all(bind=engine)

    # Add venue_id to matches table if not already there
    if inspect(engine).has_table("matches"):
        with engine.connect() as conn:
            add_column_if_missing(conn, "matches", "venue_id", "INTEGER")
            conn.commit()

    db = Session()
    try:
        inserted = updated = 0

        for v in VENUES:
            existing = db.query(Venue).filter_by(name=v["name"]).first()
            if existing:
                for field in ["fifa_name", "city", "state", "country", "capacity",
                              "matches", "roof", "nfl_tenant", "opened",
                              "region", "lat", "lon", "notes"]:
                    setattr(existing, field, v.get(field))
                venue_obj = existing
                updated += 1
            else:
                venue_obj = Venue(
                    name       = v["name"],
                    fifa_name  = v["fifa_name"],
                    city       = v["city"],
                    state      = v.get("state"),
                    country    = v["country"],
                    capacity   = v["capacity"],
                    matches    = v["matches"],
                    roof       = v["roof"],
                    nfl_tenant = v.get("nfl_tenant"),
                    opened     = v["opened"],
                    region     = v["region"],
                    lat        = v["lat"],
                    lon        = v["lon"],
                    notes      = v.get("notes"),
                )
                db.add(venue_obj)
                inserted += 1

            db.flush()  # get the id before linking matches

            # Link each match number to this venue in the matches table
            if inspect(engine).has_table("matches"):
                for match_no in v.get("match_nos", []):
                    db.execute(
                        text("UPDATE matches SET venue_id = :vid WHERE match_no = :mn"),
                        {"vid": venue_obj.id, "mn": match_no}
                    )

        db.commit()
        total = db.query(Venue).count()
        print(f"\nDone: {inserted} venues inserted, {updated} updated.")
        print(f"Total venues in database: {total}\n")

        # Summary table
        print(f"{'Stadium':<32} {'City':<16} {'Country':<8} {'Cap':>7} {'M':>3} {'Region'}")
        print("-" * 80)
        for v in db.query(Venue).order_by(Venue.country, Venue.capacity.desc()).all():
            print(
                f"{v.name:<32} {v.city:<16} {v.country:<8} "
                f"{v.capacity:>7,} {v.matches:>3} {v.region}"
            )

    except Exception as exc:
        db.rollback()
        print(f"Error: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
