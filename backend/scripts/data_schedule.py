"""
data_schedule.py
----------------
Complete FIFA World Cup 2026 match schedule — all 104 fixtures.
Source: worldcupwiki.com / FIFA official schedule (verified May 2026).

All kickoff times stored as UTC (ET + 4 hours during EDT).
Stage values: "Group Stage" | "Round of 32" | "Round of 16" |
              "Quarterfinal" | "Semifinal" | "Third Place" | "Final"
"""

SCHEDULE = [

    # =========================================================================
    # GROUP STAGE
    # =========================================================================

    # --- June 11 (Thu) -------------------------------------------------------
    {"match": 1,  "date": "2026-06-11", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Group Stage", "group": "A",
     "home": "Mexico",       "away": "South Africa",
     "venue": "Estadio Azteca", "city": "Mexico City", "country": "Mexico"},

    {"match": 2,  "date": "2026-06-11", "time_et": "22:00", "time_utc": "02:00+1",
     "stage": "Group Stage", "group": "A",
     "home": "South Korea",  "away": "Czechia",
     "venue": "Estadio Akron", "city": "Zapopan", "country": "Mexico"},

    # --- June 12 (Fri) -------------------------------------------------------
    {"match": 3,  "date": "2026-06-12", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Group Stage", "group": "B",
     "home": "Canada",       "away": "Bosnia and Herzegovina",
     "venue": "BMO Field", "city": "Toronto", "country": "Canada"},

    {"match": 4,  "date": "2026-06-12", "time_et": "21:00", "time_utc": "01:00+1",
     "stage": "Group Stage", "group": "D",
     "home": "United States", "away": "Paraguay",
     "venue": "SoFi Stadium", "city": "Inglewood", "country": "USA"},

    # --- June 13 (Sat) -------------------------------------------------------
    {"match": 5,  "date": "2026-06-13", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Group Stage", "group": "B",
     "home": "Qatar",        "away": "Switzerland",
     "venue": "Levi's Stadium", "city": "Santa Clara", "country": "USA"},

    {"match": 6,  "date": "2026-06-13", "time_et": "18:00", "time_utc": "22:00",
     "stage": "Group Stage", "group": "C",
     "home": "Brazil",       "away": "Morocco",
     "venue": "MetLife Stadium", "city": "East Rutherford", "country": "USA"},

    {"match": 7,  "date": "2026-06-13", "time_et": "21:00", "time_utc": "01:00+1",
     "stage": "Group Stage", "group": "C",
     "home": "Haiti",        "away": "Scotland",
     "venue": "Gillette Stadium", "city": "Foxborough", "country": "USA"},

    # --- June 14 (Sun) -------------------------------------------------------
    {"match": 8,  "date": "2026-06-14", "time_et": "00:00", "time_utc": "04:00",
     "stage": "Group Stage", "group": "D",
     "home": "Australia",    "away": "Turkiye",
     "venue": "BC Place", "city": "Vancouver", "country": "Canada"},

    {"match": 9,  "date": "2026-06-14", "time_et": "13:00", "time_utc": "17:00",
     "stage": "Group Stage", "group": "E",
     "home": "Germany",      "away": "Curacao",
     "venue": "NRG Stadium", "city": "Houston", "country": "USA"},

    {"match": 10, "date": "2026-06-14", "time_et": "16:00", "time_utc": "20:00",
     "stage": "Group Stage", "group": "F",
     "home": "Netherlands",  "away": "Japan",
     "venue": "AT&T Stadium", "city": "Arlington", "country": "USA"},

    {"match": 11, "date": "2026-06-14", "time_et": "19:00", "time_utc": "23:00",
     "stage": "Group Stage", "group": "E",
     "home": "Cote d'Ivoire", "away": "Ecuador",
     "venue": "Lincoln Financial Field", "city": "Philadelphia", "country": "USA"},

    {"match": 12, "date": "2026-06-14", "time_et": "22:00", "time_utc": "02:00+1",
     "stage": "Group Stage", "group": "F",
     "home": "Sweden",       "away": "Tunisia",
     "venue": "Estadio BBVA", "city": "Monterrey", "country": "Mexico"},

    # --- June 15 (Mon) -------------------------------------------------------
    {"match": 13, "date": "2026-06-15", "time_et": "12:00", "time_utc": "16:00",
     "stage": "Group Stage", "group": "H",
     "home": "Spain",        "away": "Cabo Verde",
     "venue": "Mercedes-Benz Stadium", "city": "Atlanta", "country": "USA"},

    {"match": 14, "date": "2026-06-15", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Group Stage", "group": "G",
     "home": "Belgium",      "away": "Egypt",
     "venue": "Lumen Field", "city": "Seattle", "country": "USA"},

    {"match": 15, "date": "2026-06-15", "time_et": "18:00", "time_utc": "22:00",
     "stage": "Group Stage", "group": "H",
     "home": "Saudi Arabia", "away": "Uruguay",
     "venue": "Hard Rock Stadium", "city": "Miami Gardens", "country": "USA"},

    {"match": 16, "date": "2026-06-15", "time_et": "21:00", "time_utc": "01:00+1",
     "stage": "Group Stage", "group": "G",
     "home": "Iran",         "away": "New Zealand",
     "venue": "SoFi Stadium", "city": "Inglewood", "country": "USA"},

    # --- June 16 (Tue) -------------------------------------------------------
    {"match": 17, "date": "2026-06-16", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Group Stage", "group": "I",
     "home": "France",       "away": "Senegal",
     "venue": "MetLife Stadium", "city": "East Rutherford", "country": "USA"},

    {"match": 18, "date": "2026-06-16", "time_et": "18:00", "time_utc": "22:00",
     "stage": "Group Stage", "group": "I",
     "home": "Iraq",         "away": "Norway",
     "venue": "Gillette Stadium", "city": "Foxborough", "country": "USA"},

    {"match": 19, "date": "2026-06-16", "time_et": "21:00", "time_utc": "01:00+1",
     "stage": "Group Stage", "group": "J",
     "home": "Argentina",    "away": "Algeria",
     "venue": "Arrowhead Stadium", "city": "Kansas City", "country": "USA"},

    # --- June 17 (Wed) -------------------------------------------------------
    {"match": 20, "date": "2026-06-17", "time_et": "00:00", "time_utc": "04:00",
     "stage": "Group Stage", "group": "J",
     "home": "Austria",      "away": "Jordan",
     "venue": "Levi's Stadium", "city": "Santa Clara", "country": "USA"},

    {"match": 21, "date": "2026-06-17", "time_et": "13:00", "time_utc": "17:00",
     "stage": "Group Stage", "group": "K",
     "home": "Portugal",     "away": "DR Congo",
     "venue": "NRG Stadium", "city": "Houston", "country": "USA"},

    {"match": 22, "date": "2026-06-17", "time_et": "16:00", "time_utc": "20:00",
     "stage": "Group Stage", "group": "L",
     "home": "England",      "away": "Croatia",
     "venue": "AT&T Stadium", "city": "Arlington", "country": "USA"},

    {"match": 23, "date": "2026-06-17", "time_et": "19:00", "time_utc": "23:00",
     "stage": "Group Stage", "group": "L",
     "home": "Ghana",        "away": "Panama",
     "venue": "BMO Field", "city": "Toronto", "country": "Canada"},

    {"match": 24, "date": "2026-06-17", "time_et": "22:00", "time_utc": "02:00+1",
     "stage": "Group Stage", "group": "K",
     "home": "Uzbekistan",   "away": "Colombia",
     "venue": "Estadio Azteca", "city": "Mexico City", "country": "Mexico"},

    # --- June 18 (Thu) -------------------------------------------------------
    {"match": 25, "date": "2026-06-18", "time_et": "12:00", "time_utc": "16:00",
     "stage": "Group Stage", "group": "A",
     "home": "Czechia",      "away": "South Africa",
     "venue": "Mercedes-Benz Stadium", "city": "Atlanta", "country": "USA"},

    {"match": 26, "date": "2026-06-18", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Group Stage", "group": "B",
     "home": "Switzerland",  "away": "Bosnia and Herzegovina",
     "venue": "SoFi Stadium", "city": "Inglewood", "country": "USA"},

    {"match": 27, "date": "2026-06-18", "time_et": "18:00", "time_utc": "22:00",
     "stage": "Group Stage", "group": "B",
     "home": "Canada",       "away": "Qatar",
     "venue": "BC Place", "city": "Vancouver", "country": "Canada"},

    {"match": 28, "date": "2026-06-18", "time_et": "21:00", "time_utc": "01:00+1",
     "stage": "Group Stage", "group": "A",
     "home": "Mexico",       "away": "South Korea",
     "venue": "Estadio Akron", "city": "Zapopan", "country": "Mexico"},

    # --- June 19 (Fri) -------------------------------------------------------
    {"match": 29, "date": "2026-06-19", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Group Stage", "group": "D",
     "home": "United States", "away": "Australia",
     "venue": "Lumen Field", "city": "Seattle", "country": "USA"},

    {"match": 30, "date": "2026-06-19", "time_et": "18:00", "time_utc": "22:00",
     "stage": "Group Stage", "group": "C",
     "home": "Scotland",     "away": "Morocco",
     "venue": "Gillette Stadium", "city": "Foxborough", "country": "USA"},

    {"match": 31, "date": "2026-06-19", "time_et": "20:30", "time_utc": "00:30+1",
     "stage": "Group Stage", "group": "C",
     "home": "Brazil",       "away": "Haiti",
     "venue": "Lincoln Financial Field", "city": "Philadelphia", "country": "USA"},

    {"match": 32, "date": "2026-06-19", "time_et": "23:00", "time_utc": "03:00+1",
     "stage": "Group Stage", "group": "D",
     "home": "Turkiye",      "away": "Paraguay",
     "venue": "Levi's Stadium", "city": "Santa Clara", "country": "USA"},

    # --- June 20 (Sat) -------------------------------------------------------
    {"match": 33, "date": "2026-06-20", "time_et": "13:00", "time_utc": "17:00",
     "stage": "Group Stage", "group": "F",
     "home": "Netherlands",  "away": "Sweden",
     "venue": "NRG Stadium", "city": "Houston", "country": "USA"},

    {"match": 34, "date": "2026-06-20", "time_et": "16:00", "time_utc": "20:00",
     "stage": "Group Stage", "group": "E",
     "home": "Germany",      "away": "Cote d'Ivoire",
     "venue": "BMO Field", "city": "Toronto", "country": "Canada"},

    {"match": 35, "date": "2026-06-20", "time_et": "20:00", "time_utc": "00:00+1",
     "stage": "Group Stage", "group": "E",
     "home": "Ecuador",      "away": "Curacao",
     "venue": "Arrowhead Stadium", "city": "Kansas City", "country": "USA"},

    # --- June 21 (Sun) -------------------------------------------------------
    {"match": 36, "date": "2026-06-21", "time_et": "00:00", "time_utc": "04:00",
     "stage": "Group Stage", "group": "F",
     "home": "Tunisia",      "away": "Japan",
     "venue": "Estadio BBVA", "city": "Monterrey", "country": "Mexico"},

    {"match": 37, "date": "2026-06-21", "time_et": "12:00", "time_utc": "16:00",
     "stage": "Group Stage", "group": "H",
     "home": "Spain",        "away": "Saudi Arabia",
     "venue": "Mercedes-Benz Stadium", "city": "Atlanta", "country": "USA"},

    {"match": 38, "date": "2026-06-21", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Group Stage", "group": "G",
     "home": "Belgium",      "away": "Iran",
     "venue": "SoFi Stadium", "city": "Inglewood", "country": "USA"},

    {"match": 39, "date": "2026-06-21", "time_et": "18:00", "time_utc": "22:00",
     "stage": "Group Stage", "group": "H",
     "home": "Uruguay",      "away": "Cabo Verde",
     "venue": "Hard Rock Stadium", "city": "Miami Gardens", "country": "USA"},

    {"match": 40, "date": "2026-06-21", "time_et": "21:00", "time_utc": "01:00+1",
     "stage": "Group Stage", "group": "G",
     "home": "New Zealand",  "away": "Egypt",
     "venue": "BC Place", "city": "Vancouver", "country": "Canada"},

    # --- June 22 (Mon) -------------------------------------------------------
    {"match": 41, "date": "2026-06-22", "time_et": "13:00", "time_utc": "17:00",
     "stage": "Group Stage", "group": "J",
     "home": "Argentina",    "away": "Austria",
     "venue": "AT&T Stadium", "city": "Arlington", "country": "USA"},

    {"match": 42, "date": "2026-06-22", "time_et": "17:00", "time_utc": "21:00",
     "stage": "Group Stage", "group": "I",
     "home": "France",       "away": "Iraq",
     "venue": "Lincoln Financial Field", "city": "Philadelphia", "country": "USA"},

    {"match": 43, "date": "2026-06-22", "time_et": "20:00", "time_utc": "00:00+1",
     "stage": "Group Stage", "group": "I",
     "home": "Norway",       "away": "Senegal",
     "venue": "MetLife Stadium", "city": "East Rutherford", "country": "USA"},

    {"match": 44, "date": "2026-06-22", "time_et": "23:00", "time_utc": "03:00+1",
     "stage": "Group Stage", "group": "J",
     "home": "Jordan",       "away": "Algeria",
     "venue": "Levi's Stadium", "city": "Santa Clara", "country": "USA"},

    # --- June 23 (Tue) -------------------------------------------------------
    {"match": 45, "date": "2026-06-23", "time_et": "13:00", "time_utc": "17:00",
     "stage": "Group Stage", "group": "K",
     "home": "Portugal",     "away": "Uzbekistan",
     "venue": "NRG Stadium", "city": "Houston", "country": "USA"},

    {"match": 46, "date": "2026-06-23", "time_et": "16:00", "time_utc": "20:00",
     "stage": "Group Stage", "group": "L",
     "home": "England",      "away": "Ghana",
     "venue": "Gillette Stadium", "city": "Foxborough", "country": "USA"},

    {"match": 47, "date": "2026-06-23", "time_et": "19:00", "time_utc": "23:00",
     "stage": "Group Stage", "group": "L",
     "home": "Panama",       "away": "Croatia",
     "venue": "BMO Field", "city": "Toronto", "country": "Canada"},

    {"match": 48, "date": "2026-06-23", "time_et": "22:00", "time_utc": "02:00+1",
     "stage": "Group Stage", "group": "K",
     "home": "Colombia",     "away": "DR Congo",
     "venue": "Estadio Akron", "city": "Zapopan", "country": "Mexico"},

    # --- June 24 (Wed) — Final Group Matchday --------------------------------
    {"match": 49, "date": "2026-06-24", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Group Stage", "group": "B",
     "home": "Switzerland",  "away": "Canada",
     "venue": "BC Place", "city": "Vancouver", "country": "Canada"},

    {"match": 50, "date": "2026-06-24", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Group Stage", "group": "B",
     "home": "Bosnia and Herzegovina", "away": "Qatar",
     "venue": "Lumen Field", "city": "Seattle", "country": "USA"},

    {"match": 51, "date": "2026-06-24", "time_et": "18:00", "time_utc": "22:00",
     "stage": "Group Stage", "group": "C",
     "home": "Scotland",     "away": "Brazil",
     "venue": "Hard Rock Stadium", "city": "Miami Gardens", "country": "USA"},

    {"match": 52, "date": "2026-06-24", "time_et": "18:00", "time_utc": "22:00",
     "stage": "Group Stage", "group": "C",
     "home": "Morocco",      "away": "Haiti",
     "venue": "Mercedes-Benz Stadium", "city": "Atlanta", "country": "USA"},

    {"match": 53, "date": "2026-06-24", "time_et": "21:00", "time_utc": "01:00+1",
     "stage": "Group Stage", "group": "A",
     "home": "Czechia",      "away": "Mexico",
     "venue": "Estadio Azteca", "city": "Mexico City", "country": "Mexico"},

    {"match": 54, "date": "2026-06-24", "time_et": "21:00", "time_utc": "01:00+1",
     "stage": "Group Stage", "group": "A",
     "home": "South Africa", "away": "South Korea",
     "venue": "Estadio BBVA", "city": "Monterrey", "country": "Mexico"},

    # --- June 25 (Thu) — Final Group Matchday --------------------------------
    {"match": 55, "date": "2026-06-25", "time_et": "16:00", "time_utc": "20:00",
     "stage": "Group Stage", "group": "E",
     "home": "Curacao",      "away": "Cote d'Ivoire",
     "venue": "Lincoln Financial Field", "city": "Philadelphia", "country": "USA"},

    {"match": 56, "date": "2026-06-25", "time_et": "16:00", "time_utc": "20:00",
     "stage": "Group Stage", "group": "E",
     "home": "Ecuador",      "away": "Germany",
     "venue": "MetLife Stadium", "city": "East Rutherford", "country": "USA"},

    {"match": 57, "date": "2026-06-25", "time_et": "19:00", "time_utc": "23:00",
     "stage": "Group Stage", "group": "F",
     "home": "Japan",        "away": "Sweden",
     "venue": "AT&T Stadium", "city": "Arlington", "country": "USA"},

    {"match": 58, "date": "2026-06-25", "time_et": "19:00", "time_utc": "23:00",
     "stage": "Group Stage", "group": "F",
     "home": "Tunisia",      "away": "Netherlands",
     "venue": "Arrowhead Stadium", "city": "Kansas City", "country": "USA"},

    {"match": 59, "date": "2026-06-25", "time_et": "22:00", "time_utc": "02:00+1",
     "stage": "Group Stage", "group": "D",
     "home": "Turkiye",      "away": "United States",
     "venue": "SoFi Stadium", "city": "Inglewood", "country": "USA"},

    {"match": 60, "date": "2026-06-25", "time_et": "22:00", "time_utc": "02:00+1",
     "stage": "Group Stage", "group": "D",
     "home": "Paraguay",     "away": "Australia",
     "venue": "Levi's Stadium", "city": "Santa Clara", "country": "USA"},

    # --- June 26 (Fri) — Final Group Matchday --------------------------------
    {"match": 61, "date": "2026-06-26", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Group Stage", "group": "I",
     "home": "Norway",       "away": "France",
     "venue": "Gillette Stadium", "city": "Foxborough", "country": "USA"},

    {"match": 62, "date": "2026-06-26", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Group Stage", "group": "I",
     "home": "Senegal",      "away": "Iraq",
     "venue": "BMO Field", "city": "Toronto", "country": "Canada"},

    {"match": 63, "date": "2026-06-26", "time_et": "20:00", "time_utc": "00:00+1",
     "stage": "Group Stage", "group": "H",
     "home": "Cabo Verde",   "away": "Saudi Arabia",
     "venue": "NRG Stadium", "city": "Houston", "country": "USA"},

    {"match": 64, "date": "2026-06-26", "time_et": "20:00", "time_utc": "00:00+1",
     "stage": "Group Stage", "group": "H",
     "home": "Uruguay",      "away": "Spain",
     "venue": "Estadio Akron", "city": "Zapopan", "country": "Mexico"},

    {"match": 65, "date": "2026-06-26", "time_et": "23:00", "time_utc": "03:00+1",
     "stage": "Group Stage", "group": "G",
     "home": "Egypt",        "away": "Iran",
     "venue": "Lumen Field", "city": "Seattle", "country": "USA"},

    {"match": 66, "date": "2026-06-26", "time_et": "23:00", "time_utc": "03:00+1",
     "stage": "Group Stage", "group": "G",
     "home": "New Zealand",  "away": "Belgium",
     "venue": "BC Place", "city": "Vancouver", "country": "Canada"},

    # --- June 27 (Sat) — Final Group Matchday --------------------------------
    {"match": 67, "date": "2026-06-27", "time_et": "17:00", "time_utc": "21:00",
     "stage": "Group Stage", "group": "L",
     "home": "Panama",       "away": "England",
     "venue": "MetLife Stadium", "city": "East Rutherford", "country": "USA"},

    {"match": 68, "date": "2026-06-27", "time_et": "17:00", "time_utc": "21:00",
     "stage": "Group Stage", "group": "L",
     "home": "Croatia",      "away": "Ghana",
     "venue": "Lincoln Financial Field", "city": "Philadelphia", "country": "USA"},

    {"match": 69, "date": "2026-06-27", "time_et": "19:30", "time_utc": "23:30",
     "stage": "Group Stage", "group": "K",
     "home": "Colombia",     "away": "Portugal",
     "venue": "Hard Rock Stadium", "city": "Miami Gardens", "country": "USA"},

    {"match": 70, "date": "2026-06-27", "time_et": "19:30", "time_utc": "23:30",
     "stage": "Group Stage", "group": "K",
     "home": "DR Congo",     "away": "Uzbekistan",
     "venue": "Mercedes-Benz Stadium", "city": "Atlanta", "country": "USA"},

    {"match": 71, "date": "2026-06-27", "time_et": "22:00", "time_utc": "02:00+1",
     "stage": "Group Stage", "group": "J",
     "home": "Algeria",      "away": "Austria",
     "venue": "Arrowhead Stadium", "city": "Kansas City", "country": "USA"},

    {"match": 72, "date": "2026-06-27", "time_et": "22:00", "time_utc": "02:00+1",
     "stage": "Group Stage", "group": "J",
     "home": "Jordan",       "away": "Argentina",
     "venue": "AT&T Stadium", "city": "Arlington", "country": "USA"},

    # =========================================================================
    # ROUND OF 32
    # =========================================================================

    {"match": 73, "date": "2026-06-28", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Round of 32", "group": None,
     "home": "Runner-up A",  "away": "Runner-up B",
     "venue": "SoFi Stadium", "city": "Inglewood", "country": "USA"},

    {"match": 76, "date": "2026-06-29", "time_et": "13:00", "time_utc": "17:00",
     "stage": "Round of 32", "group": None,
     "home": "Winner C",     "away": "Runner-up F",
     "venue": "NRG Stadium", "city": "Houston", "country": "USA"},

    {"match": 74, "date": "2026-06-29", "time_et": "16:30", "time_utc": "20:30",
     "stage": "Round of 32", "group": None,
     "home": "Winner E",     "away": "Best 3rd (A/B/C/D/F)",
     "venue": "Gillette Stadium", "city": "Foxborough", "country": "USA"},

    {"match": 75, "date": "2026-06-29", "time_et": "21:00", "time_utc": "01:00+1",
     "stage": "Round of 32", "group": None,
     "home": "Winner F",     "away": "Runner-up C",
     "venue": "Estadio BBVA", "city": "Monterrey", "country": "Mexico"},

    {"match": 78, "date": "2026-06-30", "time_et": "13:00", "time_utc": "17:00",
     "stage": "Round of 32", "group": None,
     "home": "Runner-up E",  "away": "Runner-up I",
     "venue": "AT&T Stadium", "city": "Arlington", "country": "USA"},

    {"match": 77, "date": "2026-06-30", "time_et": "17:00", "time_utc": "21:00",
     "stage": "Round of 32", "group": None,
     "home": "Winner I",     "away": "Best 3rd (C/D/F/G/H)",
     "venue": "MetLife Stadium", "city": "East Rutherford", "country": "USA"},

    {"match": 79, "date": "2026-06-30", "time_et": "21:00", "time_utc": "01:00+1",
     "stage": "Round of 32", "group": None,
     "home": "Winner A",     "away": "Best 3rd (C/E/F/H/I)",
     "venue": "Estadio Azteca", "city": "Mexico City", "country": "Mexico"},

    {"match": 80, "date": "2026-07-01", "time_et": "12:00", "time_utc": "16:00",
     "stage": "Round of 32", "group": None,
     "home": "Winner L",     "away": "Best 3rd (E/H/I/J/K)",
     "venue": "Mercedes-Benz Stadium", "city": "Atlanta", "country": "USA"},

    {"match": 82, "date": "2026-07-01", "time_et": "16:00", "time_utc": "20:00",
     "stage": "Round of 32", "group": None,
     "home": "Winner G",     "away": "Best 3rd (A/E/H/I/J)",
     "venue": "Lumen Field", "city": "Seattle", "country": "USA"},

    {"match": 81, "date": "2026-07-01", "time_et": "20:00", "time_utc": "00:00+1",
     "stage": "Round of 32", "group": None,
     "home": "Winner D",     "away": "Best 3rd (B/E/F/I/J)",
     "venue": "Levi's Stadium", "city": "Santa Clara", "country": "USA"},

    {"match": 84, "date": "2026-07-02", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Round of 32", "group": None,
     "home": "Winner H",     "away": "Runner-up J",
     "venue": "SoFi Stadium", "city": "Inglewood", "country": "USA"},

    {"match": 83, "date": "2026-07-02", "time_et": "19:00", "time_utc": "23:00",
     "stage": "Round of 32", "group": None,
     "home": "Runner-up K",  "away": "Runner-up L",
     "venue": "BMO Field", "city": "Toronto", "country": "Canada"},

    {"match": 85, "date": "2026-07-02", "time_et": "23:00", "time_utc": "03:00+1",
     "stage": "Round of 32", "group": None,
     "home": "Winner B",     "away": "Best 3rd (E/F/G/I/J)",
     "venue": "BC Place", "city": "Vancouver", "country": "Canada"},

    {"match": 88, "date": "2026-07-03", "time_et": "14:00", "time_utc": "18:00",
     "stage": "Round of 32", "group": None,
     "home": "Runner-up D",  "away": "Runner-up G",
     "venue": "AT&T Stadium", "city": "Arlington", "country": "USA"},

    {"match": 86, "date": "2026-07-03", "time_et": "18:00", "time_utc": "22:00",
     "stage": "Round of 32", "group": None,
     "home": "Winner J",     "away": "Runner-up H",
     "venue": "Hard Rock Stadium", "city": "Miami Gardens", "country": "USA"},

    {"match": 87, "date": "2026-07-03", "time_et": "21:30", "time_utc": "01:30+1",
     "stage": "Round of 32", "group": None,
     "home": "Winner K",     "away": "Best 3rd (D/E/I/J/L)",
     "venue": "Arrowhead Stadium", "city": "Kansas City", "country": "USA"},

    # =========================================================================
    # ROUND OF 16
    # =========================================================================

    {"match": 90, "date": "2026-07-04", "time_et": "13:00", "time_utc": "17:00",
     "stage": "Round of 16", "group": None,
     "home": "Winner M73",   "away": "Winner M75",
     "venue": "NRG Stadium", "city": "Houston", "country": "USA"},

    {"match": 89, "date": "2026-07-04", "time_et": "17:00", "time_utc": "21:00",
     "stage": "Round of 16", "group": None,
     "home": "Winner M74",   "away": "Winner M77",
     "venue": "Lincoln Financial Field", "city": "Philadelphia", "country": "USA"},

    {"match": 91, "date": "2026-07-05", "time_et": "16:00", "time_utc": "20:00",
     "stage": "Round of 16", "group": None,
     "home": "Winner M76",   "away": "Winner M78",
     "venue": "MetLife Stadium", "city": "East Rutherford", "country": "USA"},

    {"match": 92, "date": "2026-07-05", "time_et": "20:00", "time_utc": "00:00+1",
     "stage": "Round of 16", "group": None,
     "home": "Winner M79",   "away": "Winner M80",
     "venue": "Estadio Azteca", "city": "Mexico City", "country": "Mexico"},

    {"match": 93, "date": "2026-07-06", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Round of 16", "group": None,
     "home": "Winner M83",   "away": "Winner M84",
     "venue": "AT&T Stadium", "city": "Arlington", "country": "USA"},

    {"match": 94, "date": "2026-07-06", "time_et": "20:00", "time_utc": "00:00+1",
     "stage": "Round of 16", "group": None,
     "home": "Winner M81",   "away": "Winner M82",
     "venue": "Lumen Field", "city": "Seattle", "country": "USA"},

    {"match": 95, "date": "2026-07-07", "time_et": "12:00", "time_utc": "16:00",
     "stage": "Round of 16", "group": None,
     "home": "Winner M86",   "away": "Winner M88",
     "venue": "Mercedes-Benz Stadium", "city": "Atlanta", "country": "USA"},

    {"match": 96, "date": "2026-07-07", "time_et": "16:00", "time_utc": "20:00",
     "stage": "Round of 16", "group": None,
     "home": "Winner M85",   "away": "Winner M87",
     "venue": "BC Place", "city": "Vancouver", "country": "Canada"},

    # =========================================================================
    # QUARTERFINALS
    # =========================================================================

    {"match": 97,  "date": "2026-07-09", "time_et": "16:00", "time_utc": "20:00",
     "stage": "Quarterfinal", "group": None,
     "home": "Winner M89",   "away": "Winner M90",
     "venue": "Gillette Stadium", "city": "Foxborough", "country": "USA"},

    {"match": 98,  "date": "2026-07-10", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Quarterfinal", "group": None,
     "home": "Winner M93",   "away": "Winner M94",
     "venue": "SoFi Stadium", "city": "Inglewood", "country": "USA"},

    {"match": 99,  "date": "2026-07-11", "time_et": "17:00", "time_utc": "21:00",
     "stage": "Quarterfinal", "group": None,
     "home": "Winner M91",   "away": "Winner M92",
     "venue": "Hard Rock Stadium", "city": "Miami Gardens", "country": "USA"},

    {"match": 100, "date": "2026-07-11", "time_et": "21:00", "time_utc": "01:00+1",
     "stage": "Quarterfinal", "group": None,
     "home": "Winner M95",   "away": "Winner M96",
     "venue": "Arrowhead Stadium", "city": "Kansas City", "country": "USA"},

    # =========================================================================
    # SEMIFINALS
    # =========================================================================

    {"match": 101, "date": "2026-07-14", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Semifinal", "group": None,
     "home": "Winner M97",   "away": "Winner M98",
     "venue": "AT&T Stadium", "city": "Arlington", "country": "USA"},

    {"match": 102, "date": "2026-07-15", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Semifinal", "group": None,
     "home": "Winner M99",   "away": "Winner M100",
     "venue": "Mercedes-Benz Stadium", "city": "Atlanta", "country": "USA"},

    # =========================================================================
    # THIRD PLACE
    # =========================================================================

    {"match": 103, "date": "2026-07-18", "time_et": "17:00", "time_utc": "21:00",
     "stage": "Third Place", "group": None,
     "home": "Loser M101",   "away": "Loser M102",
     "venue": "Hard Rock Stadium", "city": "Miami Gardens", "country": "USA"},

    # =========================================================================
    # FINAL
    # =========================================================================

    {"match": 104, "date": "2026-07-19", "time_et": "15:00", "time_utc": "19:00",
     "stage": "Final", "group": None,
     "home": "Winner M101",  "away": "Winner M102",
     "venue": "MetLife Stadium", "city": "East Rutherford", "country": "USA"},
]
