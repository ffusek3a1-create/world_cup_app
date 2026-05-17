"""
seed_teams_v2.py
────────────────
Expands the world_cup.db schema with three new columns:
  • fifa_ranking  — official FIFA ranking (April 1, 2026 update)
  • manager       — current head coach
  • nickname      — team's official/popular nickname

Handles both fresh databases and existing ones (adds columns only if
they are missing, then upserts all 48 teams).

Run from the same directory as world_cup.db:
    python seed_teams_v2.py
"""

from sqlalchemy import (
    Column, Integer, String, text,
    create_engine, inspect
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ── Database setup ─────────────────────────────────────────────────────────────
DATABASE_URL = "sqlite:///./world_cup.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Team(Base):
    __tablename__ = "teams"
    id           = Column(Integer, primary_key=True, index=True)
    name         = Column(String, unique=True)
    group        = Column(String)
    fifa_ranking = Column(Integer)
    manager      = Column(String)
    nickname     = Column(String)


# ── All 48 teams — FIFA World Cup 2026 ────────────────────────────────────────
# FIFA ranking: April 1, 2026 official update — verified against the FIFA
#   official ranking news article (inside.fifa.com) and worldcuppass.com.
#   Key corrections vs earlier drafts: Türkiye=22, Sweden=38, Tunisia=44,
#   Côte d'Ivoire=34, Colombia=19, South Korea=23, New Zealand=85.
# Groups: confirmed after UEFA / inter-confederation play-offs (source: Al Jazeera)
# Managers: current as of May 2026 (sources: Soccerphile, Tribuna, FourFourTwo)
#   Note: Ghana's Otto Addo was sacked on 31 Mar 2026; replaced by Carlos Queiroz.
# Nicknames: official or most widely used English names.
TEAMS = [
    # ── Group A ───────────────────────────────────────────────────────────────
    {
        "name": "Mexico", "group": "A", "fifa_ranking": 15,
        "manager": "Javier Aguirre", "nickname": "El Tri",
    },
    {
        "name": "South Africa", "group": "A", "fifa_ranking": 58,
        "manager": "Hugo Broos", "nickname": "Bafana Bafana",
    },
    {
        "name": "South Korea", "group": "A", "fifa_ranking": 23,
        "manager": "Hong Myung-bo", "nickname": "Taeguk Warriors",
    },
    {
        "name": "Czechia", "group": "A", "fifa_ranking": 41,
        "manager": "Ivan Hašek", "nickname": "Národní tým",
    },

    # ── Group B ───────────────────────────────────────────────────────────────
    {
        "name": "Canada", "group": "B", "fifa_ranking": 30,
        "manager": "Jesse Marsch", "nickname": "Les Rouges",
    },
    {
        "name": "Bosnia and Herzegovina", "group": "B", "fifa_ranking": 65,
        "manager": "Sergej Barbarez", "nickname": "Zmajevi (The Dragons)",
    },
    {
        "name": "Qatar", "group": "B", "fifa_ranking": 36,
        "manager": "Julen Lopetegui", "nickname": "The Maroons",
    },
    {
        "name": "Switzerland", "group": "B", "fifa_ranking": 14,
        "manager": "Murat Yakin", "nickname": "Nati",
    },

    # ── Group C ───────────────────────────────────────────────────────────────
    {
        "name": "Brazil", "group": "C", "fifa_ranking": 6,
        "manager": "Carlo Ancelotti", "nickname": "Seleção / Canarinhos",
    },
    {
        "name": "Morocco", "group": "C", "fifa_ranking": 8,
        "manager": "Walid Regragui", "nickname": "Atlas Lions",
    },
    {
        "name": "Haiti", "group": "C", "fifa_ranking": 83,
        "manager": "Sébastien Migné", "nickname": "Les Grenadiers",
    },
    {
        "name": "Scotland", "group": "C", "fifa_ranking": 47,
        "manager": "Steve Clarke", "nickname": "The Tartan Army",
    },

    # ── Group D ───────────────────────────────────────────────────────────────
    {
        "name": "United States", "group": "D", "fifa_ranking": 16,
        "manager": "Mauricio Pochettino", "nickname": "The Stars and Stripes",
    },
    {
        "name": "Paraguay", "group": "D", "fifa_ranking": 56,
        "manager": "Gustavo Alfaro", "nickname": "La Albirroja",
    },
    {
        "name": "Australia", "group": "D", "fifa_ranking": 24,
        "manager": "Tony Popovic", "nickname": "The Socceroos",
    },
    {
        "name": "Türkiye", "group": "D", "fifa_ranking": 22,
        "manager": "Vincenzo Montella", "nickname": "Ay-Yıldızlılar (The Crescent-Stars)",
    },

    # ── Group E ───────────────────────────────────────────────────────────────
    {
        "name": "Germany", "group": "E", "fifa_ranking": 10,
        "manager": "Julian Nagelsmann", "nickname": "Die Mannschaft",
    },
    {
        "name": "Curacao", "group": "E", "fifa_ranking": 82,
        "manager": "Dick Advocaat", "nickname": "The Brave Boys",
    },
    {
        "name": "Cote d'Ivoire", "group": "E", "fifa_ranking": 34,
        "manager": "Emerse Faé", "nickname": "Les Éléphants",
    },
    {
        "name": "Ecuador", "group": "E", "fifa_ranking": 28,
        "manager": "Sebastián Beccacece", "nickname": "La Tri",
    },

    # ── Group F ───────────────────────────────────────────────────────────────
    {
        "name": "Netherlands", "group": "F", "fifa_ranking": 7,
        "manager": "Ronald Koeman", "nickname": "Oranje",
    },
    {
        "name": "Japan", "group": "F", "fifa_ranking": 17,
        "manager": "Hajime Moriyasu", "nickname": "Samurai Blue",
    },
    {
        "name": "Sweden", "group": "F", "fifa_ranking": 38,
        "manager": "Graham Potter", "nickname": "Blågult (Blue and Yellow)",
    },
    {
        "name": "Tunisia", "group": "F", "fifa_ranking": 44,
        "manager": "Faouzi Benzarti", "nickname": "Les Aigles de Carthage",
    },

    # ── Group G ───────────────────────────────────────────────────────────────
    {
        "name": "Belgium", "group": "G", "fifa_ranking": 9,
        "manager": "Rudi Garcia", "nickname": "Les Diables Rouges / Rode Duivels",
    },
    {
        "name": "Egypt", "group": "G", "fifa_ranking": 29,
        "manager": "Hossam Hassan", "nickname": "The Pharaohs",
    },
    {
        "name": "Iran", "group": "G", "fifa_ranking": 18,
        "manager": "Amir Ghalenoei", "nickname": "Team Melli",
    },
    {
        "name": "New Zealand", "group": "G", "fifa_ranking": 85,
        "manager": "Darren Bazeley", "nickname": "All Whites",
    },

    # ── Group H ───────────────────────────────────────────────────────────────
    {
        "name": "Spain", "group": "H", "fifa_ranking": 2,
        "manager": "Luis de la Fuente", "nickname": "La Roja",
    },
    {
        "name": "Cabo Verde", "group": "H", "fifa_ranking": 69,
        "manager": "Bubista", "nickname": "Tubarões Azuis (Blue Sharks)",
    },
    {
        "name": "Saudi Arabia", "group": "H", "fifa_ranking": 57,
        "manager": "Hervé Renard", "nickname": "Al-Suqour (The Falcons)",
    },
    {
        "name": "Uruguay", "group": "H", "fifa_ranking": 13,
        "manager": "Marcelo Bielsa", "nickname": "La Celeste",
    },

    # ── Group I ───────────────────────────────────────────────────────────────
    {
        "name": "France", "group": "I", "fifa_ranking": 1,
        "manager": "Didier Deschamps", "nickname": "Les Bleus",
    },
    {
        "name": "Senegal", "group": "I", "fifa_ranking": 21,
        "manager": "Pape Thiaw", "nickname": "Lions of Teranga",
    },
    {
        "name": "Iraq", "group": "I", "fifa_ranking": 60,
        "manager": "Graham Arnold", "nickname": "Usud Al-Rafidayn (Lions of Mesopotamia)",
    },
    {
        "name": "Norway", "group": "I", "fifa_ranking": 44,
        "manager": "Ståle Solbakken", "nickname": "Løvene (The Lions)",
    },

    # ── Group J ───────────────────────────────────────────────────────────────
    {
        "name": "Argentina", "group": "J", "fifa_ranking": 3,
        "manager": "Lionel Scaloni", "nickname": "La Albiceleste",
    },
    {
        "name": "Algeria", "group": "J", "fifa_ranking": 36,
        "manager": "Vladimir Petković", "nickname": "Les Fennecs",
    },
    {
        "name": "Austria", "group": "J", "fifa_ranking": 23,
        "manager": "Ralf Rangnick", "nickname": "Das Team",
    },
    {
        "name": "Jordan", "group": "J", "fifa_ranking": 67,
        "manager": "Jamal Sellami", "nickname": "Al-Nashama (The Brave Ones)",
    },

    # ── Group K ───────────────────────────────────────────────────────────────
    {
        "name": "Portugal", "group": "K", "fifa_ranking": 5,
        "manager": "Roberto Martínez", "nickname": "A Seleção das Quinas",
    },
    {
        "name": "DR Congo", "group": "K", "fifa_ranking": 54,
        "manager": "Sébastien Desabre", "nickname": "Les Léopards",
    },
    {
        "name": "Uzbekistan", "group": "K", "fifa_ranking": 63,
        "manager": "Fabio Cannavaro", "nickname": "White Wolves",
    },
    {
        "name": "Colombia", "group": "K", "fifa_ranking": 19,
        "manager": "Néstor Lorenzo", "nickname": "Los Cafeteros",
    },

    # ── Group L ───────────────────────────────────────────────────────────────
    {
        "name": "England", "group": "L", "fifa_ranking": 4,
        "manager": "Thomas Tuchel", "nickname": "The Three Lions",
    },
    {
        "name": "Croatia", "group": "L", "fifa_ranking": 11,
        "manager": "Zlatko Dalić", "nickname": "Vatreni (The Blazers)",
    },
    {
        "name": "Ghana", "group": "L", "fifa_ranking": 74,
        "manager": "Carlos Queiroz", "nickname": "Black Stars",
    },
    {
        "name": "Panama", "group": "L", "fifa_ranking": 53,
        "manager": "Thomas Christiansen", "nickname": "Los Canaleros",
    },
]


def _add_column_if_missing(conn, table: str, column: str, col_type: str):
    """Add a column to an existing SQLite table if it doesn't already exist."""
    inspector = inspect(engine)
    existing = [c["name"] for c in inspector.get_columns(table)]
    if column not in existing:
        conn.execute(text(f"ALTER TABLE {table} ADD COLUMN {column} {col_type}"))
        print(f"  ✚ Added column '{column}' to '{table}'.")


def seed():
    # Ensure the table exists (creates it on a fresh DB)
    Base.metadata.create_all(bind=engine)

    # Migrate existing DB: add new columns if they're missing
    with engine.connect() as conn:
        _add_column_if_missing(conn, "teams", "fifa_ranking", "INTEGER")
        _add_column_if_missing(conn, "teams", "manager",      "VARCHAR")
        _add_column_if_missing(conn, "teams", "nickname",     "VARCHAR")
        conn.commit()

    db = SessionLocal()
    try:
        inserted = 0
        updated  = 0

        for data in TEAMS:
            team = db.query(Team).filter_by(name=data["name"]).first()
            if team:
                # Update all fields on existing rows
                team.group        = data["group"]
                team.fifa_ranking = data["fifa_ranking"]
                team.manager      = data["manager"]
                team.nickname     = data["nickname"]
                updated += 1
            else:
                db.add(Team(**data))
                inserted += 1

        db.commit()
        total = db.query(Team).count()
        print(
            f"\n✅  Done: {inserted} teams inserted, {updated} updated.\n"
            f"    Total teams in database: {total}\n"
        )

        # Pretty-print a quick summary table
        print(f"{'#':<5} {'Group':<7} {'Rank':<6} {'Team':<30} {'Manager':<25} {'Nickname'}")
        print("-" * 110)
        for t in sorted(db.query(Team).all(), key=lambda x: (x.group, x.fifa_ranking or 999)):
            print(
                f"{t.id:<5} {t.group:<7} {str(t.fifa_ranking):<6} "
                f"{t.name:<30} {(t.manager or ''):<25} {t.nickname or ''}"
            )

    except Exception as exc:
        db.rollback()
        print(f"❌  Error: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()