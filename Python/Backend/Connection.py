import sqlite3

class SqliteConnection:
    def __init__(self,name):
        self.name = name
        
    def establishConnection(dbName):
        dbName = dbName +".db"
        conn = sqlite3.connect(dbName)
        cur = conn.cursor()
        # cur.execute("create table if not exist (name text,surname text,username text,password text)")
        conn.commit()
        conn.close()

class Postgres:
    def __init__(self):
        pass