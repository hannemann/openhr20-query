import sys
from query.db import Db, sqlite3

class Simple(Db):
    
    valve = 0
    
    def __init__(self, valve):
        Db.__init__(self)
        self.valve = valve
    
    def fetch(self):
        try:
            self.cursor.execute(self.query, (self.valve,))
        except sqlite3.OperationalError:
            print("SQLite operational error. Database file invalid or not found")
            sys.exit(1);
        result = self.cursor.fetchone()
        if result is not None:
            return result[0]
        else:
            return 'valve ' + str(self.valve) + 'not found'
        
    def __str__(self):
        value = self.fetch()
        self.close()
        return self.format(value)
    
    def format(self, value):
        return str(value)