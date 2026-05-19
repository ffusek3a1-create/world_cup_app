import sqlite3, os
conn = sqlite3.connect('world_cup.db')
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print('Tables:', tables)
print('DB location:', os.path.abspath('world_cup.db'))