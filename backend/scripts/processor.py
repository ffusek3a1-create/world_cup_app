"""
processor.py
------------
Reads results.csv (Kaggle: martj42/international-football-results-from-1872-to-2017)
and produces two enriched data structures for each team:

  1. recent_form     - last 5 matches of ANY type
  2. qualifier_path  - all FIFA World Cup 2026 qualification matches
                       (filtered from 2023-01-01 onwards)

Output: data/team_performance.json
"""

import pandas as pd
import json
import os

# -- Paths ---------------------------------------------------------------------
BASE_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FILE  = os.path.join(BASE_DIR, 'raw_data', 'results.csv')
OUTPUT_FILE = os.path.join(BASE_DIR, 'data', 'team_performance.json')

# -- Team list (keep in sync with data_teams.py / your DB) --------------------
TEAMS = [
    "Mexico", "South Africa", "South Korea", "Czech Republic",
    "Canada", "Bosnia and Herzegovina", "Qatar", "Switzerland",
    "Brazil", "Morocco", "Haiti", "Scotland",
    "United States", "Paraguay", "Australia", "Turkey",
    "Germany", "Curaçao", "Ivory Coast", "Ecuador",
    "Netherlands", "Japan", "Sweden", "Tunisia",
    "Belgium", "Egypt", "Iran", "New Zealand",
    "Spain", "Cape Verde", "Saudi Arabia", "Uruguay",
    "France", "Senegal", "Iraq", "Norway",
    "Argentina", "Algeria", "Austria", "Jordan",
    "Portugal", "DR Congo", "Uzbekistan", "Colombia",
    "England", "Croatia", "Ghana", "Panama",
]

# Maps CSV team names -> your DB/JSON team names where they differ
NAME_MAP = {
    "Turkey":       "Turkiye",
    "Ivory Coast": "Cote d'Ivoire",
    "Cape Verde":  "Cabo Verde",
    "USA":         "United States",
}

WC_APPEARANCES = {
    "Brazil": 23, "Germany": 21, "Argentina": 20,
    "Spain": 18, "Mexico": 18, "England": 17, "France": 17,
    "Uruguay": 16, "Belgium": 15, "Sweden": 13, "Switzerland": 13,
    "Netherlands": 12, "United States": 12, "South Korea": 12,
    "Portugal": 10, "Paraguay":10, "Austria": 9, "Scotland": 9, 
    "Morocco": 8, "Japan": 8, "Colombia": 7, "Croatia": 7, "Tunisia": 7, "Australia": 7,
    "Saudi Arabia": 7, "Iran": 7, "Ecuador": 5, "Algeria":5,
    "Ghana": 5, "Norway": 4, "Senegal": 4, "Ivory Coast": 4,
    "Egypt": 4, "South Africa": 4, "Turkey": 3,
    "Canada": 3, "New Zealand": 3, "Czech Republic": 2,
    "Bosnia and Herzegovina": 2, "Haiti": 2, "Panama": 2,
    "Iraq": 2, "Qatar": 2, "Democratic Republic of the Congo": 1,
    "Uzbekistan": 1, "Cape Verde": 1, "Curaçao": 1, "Jordan": 1
}

QUALIFIER_TOURNAMENT = "FIFA World Cup qualification"


def get_result(row, team):
    """Return a match result dict from the perspective of `team`."""
    is_home = row["home_team"] == team

    # Since we use dropna() in the main function, we can safely assume scores exist
    my_goals  = int(row["home_score"]) if is_home else int(row["away_score"])
    opp_goals = int(row["away_score"]) if is_home else int(row["home_score"])
    opponent  = row["away_team"]       if is_home else row["home_team"]
    venue     = "H" if is_home else "A"

    if my_goals > opp_goals:
        outcome = "W"
    elif my_goals == opp_goals:
        outcome = "D"
    else:
        outcome = "L"

    return {
        "date":       row["date"].strftime("%Y-%m-%d"),
        "opponent":   NAME_MAP.get(opponent, opponent),
        "score":      f"{my_goals}:{opp_goals}",
        "venue":      venue,
        "outcome":    outcome,
        "tournament": row["tournament"],
        "neutral":    bool(row.get("neutral", False)),
    }


def process_football_data():
    if not os.path.exists(INPUT_FILE):
        print(f"ERROR: File not found: {INPUT_FILE}")
        return

    print("🚀 Reading CSV ...")
    df = pd.read_csv(INPUT_FILE)
    df["date"] = pd.to_datetime(df["date"])

    # --- DATA CLEANING & FUTURE FILTERING ---
    # 1. Remove matches from the future
    today = pd.Timestamp.now()
    df = df[df['date'] <= today]

    # 2. Remove any matches with missing scores (NaN) to prevent ValueError
    df = df.dropna(subset=['home_score', 'away_score'])
    
    # 2026 WC qualifier matches
    qualifiers_df = df[
        (df["tournament"] == QUALIFIER_TOURNAMENT) &
        (df["date"] >= "2023-01-01")
    ].copy()
    
    print(f"    {len(df):,} completed matches | {len(qualifiers_df):,} WC 2026 qualifiers found")

    results = []

    for team in TEAMS:
        # -- All matches for this team
        team_mask = (df["home_team"] == team) | (df["away_team"] == team)
        team_all  = df[team_mask].sort_values("date")

        # -- Qualifier matches for this team
        qual_mask  = (qualifiers_df["home_team"] == team) | (qualifiers_df["away_team"] == team)
        team_quals = qualifiers_df[qual_mask].sort_values("date")

        if team_all.empty:
            print(f"WARNING: No matches found for: {team}")
            continue

        # -- Recent form: last 5 completed matches
        last_5 = team_all.tail(5)
        recent_form = [get_result(row, team) for _, row in last_5.iterrows()]

        # -- Qualifier path
        qualifier_matches = [get_result(row, team) for _, row in team_quals.iterrows()]

        # Summary stats
        w  = sum(1 for m in qualifier_matches if m["outcome"] == "W")
        d  = sum(1 for m in qualifier_matches if m["outcome"] == "D")
        l  = sum(1 for m in qualifier_matches if m["outcome"] == "L")
        gf = sum(int(m["score"].split(":")[0]) for m in qualifier_matches)
        ga = sum(int(m["score"].split(":")[1]) for m in qualifier_matches)

        db_name = NAME_MAP.get(team, team)

        appearances = WC_APPEARANCES.get(db_name, WC_APPEARANCES.get(team, 0))

        entry = {
            "name": db_name,
            "recent_form": {
                "matches":      recent_form,
                "form_string":  "".join(m["outcome"] for m in recent_form),
                "last_updated": recent_form[-1]["date"] if recent_form else None,
            },
            "qualifier_path": {
                "matches":         qualifier_matches,
                "played":          len(qualifier_matches),
                "record":          {"W": w, "D": d, "L": l},
                "goals_for":       gf,
                "goals_against":   ga,
                "goal_difference": gf - ga,
            },
        }

        results.append(entry)
        form_str = "".join(m["outcome"] for m in recent_form)
        print(f"OK  {db_name:<30}  form: {form_str:<5}  |  qualifiers: {len(qualifier_matches)}")

    # -- Write output
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    print(f"\n✅ Saved {len(results)} team entries -> {OUTPUT_FILE}")


if __name__ == "__main__":
    process_football_data()