from Backend import Connection, Update, Create
class MainCrud:
    Connection.SqliteConnection("crud")
    
    def UpdateRecord():
        Update.Update('lamin','jatta','jatta-njie21')
    
    def AddRecord():
        Create.Create('TableName?')
    
    def DeleteRecord():
        pass
    
    def SearchRecord():
        pass
    
        