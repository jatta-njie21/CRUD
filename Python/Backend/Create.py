from Backend.Connection import SqliteConnection

class Create:
    def __init__(self,y):
        self.y = y
       

    def Create(tableName):
        SqliteConnection.establishConnection("test")
        
Create()
