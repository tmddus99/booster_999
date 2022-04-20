import pymysql

class Database():
    def __init__(self):
        self._db = pymysql.connect(host = 'localhost',
                                   user = 'root',
                                   password = 'kto0812130?',
                                   db = "ubion")
        self.cursor = self._db.cursor(pymysql.cursors.DictCursor)
    
    def execute(self, _sql, _values={}):
        self.cursor.execute(_sql, _values)

    def executeAll(self, _sql, _values={}):
        self.cursor.execute(_sql, _values)
        self.result = self.cursor.fetchall()
        return self.result

    def commit(self):
        self._db.commit()