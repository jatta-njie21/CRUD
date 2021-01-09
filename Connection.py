import sqlite3

class SqliteConnection:
    conn = sqlite3.connection("crud.db")
    cur = conn.cursor()
    cur.execute("create table if not exists crud(name text,surname text,username text,password text)")
    conn.close()
