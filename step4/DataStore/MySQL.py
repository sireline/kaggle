import mysql.connector

class MySQL:    
    def __init__(self):
        self.dns = None
        self.dbh = None
    
    def open(self, **dns):
        self.dns = dns
        self.dbh = mysql.connector.connect(**self.dns)
    
    def close(self):
        self.dbh.close()

    def query(self, stmt, *args, **kwargs):
        if kwargs.get('prepared', False):
            cursor = self.dbh.cursor(prepared=True)
            cursor.execute(stmt, args)
        else:
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
        data = cursor.fetchall()
        cursor.close()
        return data
