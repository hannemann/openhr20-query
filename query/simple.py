import sys
from query.db import Db, sqlite3

class Simple(Db):
    
    valve = 0
    
    query = 'SELECT * FROM log WHERE addr=? ORDER BY time DESC LIMIT 1'
    
    def __init__(self, valve):
        Db.__init__(self)
        self.valve = valve
    
    def fetch(self):
        try:
            self.cursor.execute(self.query, (self.valve,))
        except sqlite3.OperationalError:
            print("SQLite operational error. Database file invalid or not found")
            sys.exit(1);
        row = self.cursor.fetchone()
        if row is not None:
            return row
        else:
            return 'valve ' + str(self.valve) + 'not found'
        
    def __str__(self):
        value = self.fetch()
        self.close()
        return self.format(value)
    