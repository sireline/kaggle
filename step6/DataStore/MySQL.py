import mysql.connector

class MySQL:
    def __init__(self, **dns):
        self.dns = dns
        self.dbh = None

    def _open(self):
        self.dbh = mysql.connector.MySQLConnection(**self.dns)

    def _close(self):
        self.dbh.close()

    def insert(self, stmt, *args, **kwargs):
        self._open()
        if kwargs.get('prepared', False):
            cursor = self.dbh.cursor(prepared=True)
            cursor.execute(stmt, args)
        else:
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
        self.dbh.commit()
        cursor.close()
        self._close()
        return "Data inserted."

    def select(self, stmt, *args, **kwargs):
        self._open()
        if kwargs.get('prepared', False):
            cursor = self.dbh.cursor(prepared=True)
            cursor.execute(stmt, args)
        else:
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
        keys = cursor.column_names
        rows = cursor.fetchall()
        data = []
        for row in rows:
            data.append(dict(zip(keys, row)))
        print(data)
        cursor.close()
        self._close()
        return data

    def update(self, stmt, *args, **kwargs):
        self._open()
        if kwargs.get('prepared', False):
            cursor = self.dbh.cursor(prepared=True)
            cursor.execute(stmt, args)
        else:
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
        self.dbh.commit()
        cursor.close()
        self._close()
        return "Data updated."

    def delete(self, stmt, *args, **kwargs):
        self._open()
        if kwargs.get('prepared', False):
            cursor = self.dbh.cursor(prepared=True)
            cursor.execute(stmt, args)
        else:
            cursor = self.dbh.cursor()
            cursor.execute(stmt)
        self.dbh.commit()
        cursor.close()
        self._close()
        return "Data deleted."
