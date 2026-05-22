import sqlite3, os
DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "world_cup.db")
conn = sqlite3.connect(DB)
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print("Tables:", [t[0] for t in tables])
print("DB location:", DB)
conn.close()
