from .Connection import SqliteConnection

class Update:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def update(self):
        cur.execute("update into name where name,surname,username = ?,?,?",(slef.x,self.y,self.z))
        conn.commit()
        conn.close()
    