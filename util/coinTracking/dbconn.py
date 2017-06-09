import sqlite3

class DBCONN:
    def connect(self):
        self.conn = sqlite3.connect('coin.db')
        self.cur  = self.conn.cursor()

    def disconnect(self):
        self.conn.close()
