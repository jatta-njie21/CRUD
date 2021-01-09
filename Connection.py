import sqlite3

class SqliteConnection:
    def __init__(self,name):
        self.name = name
        
    def establishConnection(dbName):
        conn = sqlite3.connect(dbName,".db")
        cur = conn.cursor()
        cur.execute("create table if not exist crud(name text,surname text,username text,password text)")
        conn.commit()
        conn.close()

class Postgres:
    def __init__(self):
        pass