"""
seed_squads.py
--------------
Reads data_squads.py and seeds a Player table into world_cup.db.
Safe to re-run: existing players are updated, not duplicated.

Schema added:
  players
    id          INTEGER PK
    team_name   VARCHAR  (FK-compatible with teams.name)
    name        VARCHAR
    club        VARCHAR
    position    VARCHAR  ("Goalkeeper" | "Defender" | "Midfielder" | "Forward")
    squad_status VARCHAR ("final" | "preliminary" | "pending")

Run from the same directory as world_cup.db:
    python seed_squads.py
"""

import sys
import os

# Allow importing data_squads from the same directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_squads import SQUADS

from sqlalchemy import Column, Integer, String, create_engine, inspect, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ── Database setup ─────────────────────────────────────────────────────────────
DATABASE_URL = "sqlite:///../world_cup.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

POSITION_MAP = {
    "goalkeepers": "Goalkeeper",
    "defenders":   "Defender",
    "midfielders": "Midfielder",
    "forwards":    "Forward",
}


class Player(Base):
    __tablename__ = "players"
    id           = Column(Integer, primary_key=True, index=True)
    team_name    = Column(String, index=True)
    name         = Column(String)
    club         = Column(String)
    position     = Column(String)
    squad_status = Column(String)   # mirrors the team's overall squad status


def seed():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        inserted = updated = skipped = 0

        for team_name, data in SQUADS.items():
            status = data["status"]
            squad  = data.get("squad", {})

            if not squad:
                skipped += 1
                continue

            for pos_key, players in squad.items():
                position = POSITION_MAP.get(pos_key, pos_key.capitalize())

                for p in players:
                    existing = (
                        db.query(Player)
                        .filter_by(team_name=team_name, name=p["name"])
                        .first()
                    )
                    if existing:
                        existing.club         = p["club"]
                        existing.position     = position
                        existing.squad_status = status
                        updated += 1
                    else:
                        db.add(Player(
                            team_name    = team_name,
                            name         = p["name"],
                            club         = p["club"],
                            position     = position,
                            squad_status = status,
                        ))
                        inserted += 1

        db.commit()
        total = db.query(Player).count()
        print(
            f"\nDone: {inserted} players inserted, {updated} updated, "
            f"{skipped} teams still pending.\n"
            f"Total players in database: {total}\n"
        )

        # Summary by team
        print(f"{'Team':<30} {'Status':<14} {'GK':>3} {'DEF':>4} {'MID':>4} {'FWD':>4} {'TOT':>4}")
        print("-" * 68)
        for team_name in SQUADS:
            rows = db.query(Player).filter_by(team_name=team_name).all()
            if not rows:
                print(f"{team_name:<30} {'pending':<14} {'—':>3} {'—':>4} {'—':>4} {'—':>4} {'—':>4}")
                continue
            gk  = sum(1 for r in rows if r.position == "Goalkeeper")
            df  = sum(1 for r in rows if r.position == "Defender")
            mf  = sum(1 for r in rows if r.position == "Midfielder")
            fw  = sum(1 for r in rows if r.position == "Forward")
            print(
                f"{team_name:<30} {rows[0].squad_status:<14} "
                f"{gk:>3} {df:>4} {mf:>4} {fw:>4} {len(rows):>4}"
            )

    except Exception as exc:
        db.rollback()
        print(f"Error: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
