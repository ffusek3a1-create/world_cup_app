import sqlite3
conn = sqlite3.connect('world_cup.db')
rows = conn.execute('''
    SELECT v.name, v.city, m.match_no, m.date, m.stage, m.home, m.away
    FROM matches m
    JOIN venues v ON m.venue_id = v.id
    ORDER BY v.name, m.match_no
''').fetchall()
current_venue = None
for r in rows:
    if r[0] != current_venue:
        current_venue = r[0]
        print(f'\n{r[0]} ({r[1]})')
        print('-' * 50)
    print(f'  #{r[2]:>3}  {r[3]}  {r[5]} vs {r[6]}  [{r[4]}]')
conn.close()