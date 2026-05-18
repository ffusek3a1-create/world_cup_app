"""
seed_schedule.py
----------------
Seeds the 'matches' table in world_cup.db from data_schedule.py.
Safe to re-run — existing rows are updated, not duplicated.

Schema:
  matches
    id          INTEGER PK
    match_no    INTEGER  (official FIFA match number, 1-104)
    date        VARCHAR  (YYYY-MM-DD)
    time_et     VARCHAR  (HH:MM Eastern Time)
    time_utc    VARCHAR  (HH:MM UTC, "+1" suffix = next day)
    stage       VARCHAR  (Group Stage / Round of 32 / Round of 16 /
                          Quarterfinal / Semifinal / Third Place / Final)
    group_name  VARCHAR  (A-L for group stage, NULL for knockout)
    home        VARCHAR  (team name or placeholder e.g. "Winner A")
    away        VARCHAR
    venue       VARCHAR
    city        VARCHAR
    country     VARCHAR
    home_score  INTEGER  (NULL until played)
    away_score  INTEGER  (NULL until played)

Run from the backend/ directory:
    python scripts/seed_schedule.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_schedule import SCHEDULE

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ── DB path: go up one level from scripts/ to backend/ ────────────────────────
DATABASE_URL = "sqlite:///../world_cup.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Match(Base):
    __tablename__ = "matches"
    id          = Column(Integer, primary_key=True, index=True)
    match_no    = Column(Integer, unique=True, index=True)
    date        = Column(String)
    time_et     = Column(String)
    time_utc    = Column(String)
    stage       = Column(String)
    group_name  = Column(String, nullable=True)
    home        = Column(String)
    away        = Column(String)
    venue       = Column(String)
    city        = Column(String)
    country     = Column(String)
    home_score  = Column(Integer, nullable=True)
    away_score  = Column(Integer, nullable=True)


def seed():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        inserted = updated = 0

        for m in SCHEDULE:
            existing = db.query(Match).filter_by(match_no=m["match"]).first()
            if existing:
                existing.date       = m["date"]
                existing.time_et    = m["time_et"]
                existing.time_utc   = m["time_utc"]
                existing.stage      = m["stage"]
                existing.group_name = m.get("group")
                existing.home       = m["home"]
                existing.away       = m["away"]
                existing.venue      = m["venue"]
                existing.city       = m["city"]
                existing.country    = m["country"]
                updated += 1
            else:
                db.add(Match(
                    match_no    = m["match"],
                    date        = m["date"],
                    time_et     = m["time_et"],
                    time_utc    = m["time_utc"],
                    stage       = m["stage"],
                    group_name  = m.get("group"),
                    home        = m["home"],
                    away        = m["away"],
                    venue       = m["venue"],
                    city        = m["city"],
                    country     = m["country"],
                    home_score  = None,
                    away_score  = None,
                ))
                inserted += 1

        db.commit()
        total = db.query(Match).count()
        print(f"\nDone: {inserted} matches inserted, {updated} updated.")
        print(f"Total matches in database: {total}\n")

        # Summary by stage
        stages = [
            "Group Stage", "Round of 32", "Round of 16",
            "Quarterfinal", "Semifinal", "Third Place", "Final"
        ]
        print(f"{'Stage':<16} {'Matches':>7}")
        print("-" * 25)
        for stage in stages:
            count = db.query(Match).filter_by(stage=stage).count()
            print(f"{stage:<16} {count:>7}")

        print()
        print("First 5 fixtures:")
        for m in db.query(Match).order_by(Match.match_no).limit(5).all():
            print(f"  #{m.match_no:>3}  {m.date}  {m.time_et} ET  "
                  f"{m.home} vs {m.away}  [{m.venue}, {m.city}]")

    except Exception as exc:
        db.rollback()
        print(f"Error: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
