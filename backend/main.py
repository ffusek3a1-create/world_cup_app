"""
main.py
-------
FastAPI backend for the World Cup 2026 app.
Run from the backend/ folder:
    uvicorn main:app --reload

Endpoints:
  GET /teams              - all 48 teams
  GET /teams/{name}       - single team + their players
  GET /groups             - all teams grouped by A-L
  GET /matches            - full schedule (optional ?stage= filter)
  GET /matches/{match_no} - single match
  GET /venues             - all 16 stadiums + their matches
  GET /venues/{name}      - single stadium + its matches
"""

import os
import sqlite3
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="World Cup 2026 API")

# Allow the React dev server to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "world_cup.db")


def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row   # lets us return dicts instead of tuples
    return conn


# ── /teams ────────────────────────────────────────────────────────────────────

@app.get("/teams")
def list_teams():
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM teams ORDER BY `group`, fifa_ranking"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


@app.get("/teams/{name}")
def get_team(name: str):
    conn = get_db()
    team = conn.execute(
        "SELECT * FROM teams WHERE name = ?", (name,)
    ).fetchone()
    if not team:
        raise HTTPException(status_code=404, detail=f"Team '{name}' not found")

    players = conn.execute(
        "SELECT name, club, position FROM players WHERE team_name = ? ORDER BY position, name",
        (name,)
    ).fetchall()
    conn.close()

    result = dict(team)
    result["players"] = {
        "Goalkeeper": [],
        "Defender":   [],
        "Midfielder": [],
        "Forward":    [],
    }
    for p in players:
        pos = p["position"]
        if pos in result["players"]:
            result["players"][pos].append({"name": p["name"], "club": p["club"]})
    return result


# ── /groups ───────────────────────────────────────────────────────────────────

@app.get("/groups")
def list_groups():
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM teams ORDER BY `group`, fifa_ranking"
    ).fetchall()
    conn.close()

    groups = {}
    for r in rows:
        g = r["group"]
        if g not in groups:
            groups[g] = []
        groups[g].append(dict(r))
    return groups


# ── /matches ──────────────────────────────────────────────────────────────────

@app.get("/matches")
def list_matches(stage: str = None):
    conn = get_db()
    if stage:
        rows = conn.execute(
            "SELECT * FROM matches WHERE stage = ? ORDER BY match_no",
            (stage,)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM matches ORDER BY match_no"
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


@app.get("/matches/{match_no}")
def get_match(match_no: int):
    conn = get_db()
    match = conn.execute(
        "SELECT * FROM matches WHERE match_no = ?", (match_no,)
    ).fetchone()
    conn.close()
    if not match:
        raise HTTPException(status_code=404, detail=f"Match #{match_no} not found")
    return dict(match)


# ── /venues ───────────────────────────────────────────────────────────────────

@app.get("/venues")
def list_venues():
    conn = get_db()
    venues = conn.execute(
        "SELECT * FROM venues ORDER BY country, city"
    ).fetchall()

    result = []
    for v in venues:
        venue_dict = dict(v)
        matches = conn.execute(
            """SELECT match_no, date, time_et, stage, group_name, home, away
               FROM matches WHERE venue_id = ?
               ORDER BY match_no""",
            (v["id"],)
        ).fetchall()
        venue_dict["matches"] = [dict(m) for m in matches]
        result.append(venue_dict)

    conn.close()
    return result


@app.get("/venues/{name}")
def get_venue(name: str):
    conn = get_db()
    venue = conn.execute(
        "SELECT * FROM venues WHERE name = ?", (name,)
    ).fetchone()
    if not venue:
        raise HTTPException(status_code=404, detail=f"Venue '{name}' not found")

    matches = conn.execute(
        """SELECT match_no, date, time_et, stage, group_name, home, away
           FROM matches WHERE venue_id = ?
           ORDER BY match_no""",
        (venue["id"],)
    ).fetchall()
    conn.close()

    result = dict(venue)
    result["matches"] = [dict(m) for m in matches]
    return result