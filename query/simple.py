import sys
from query.db import Db, sqlite3
from config import config

class Simple(Db):
    
    valve = 0
    
    query = 'SELECT * FROM log WHERE addr=? ORDER BY time DESC LIMIT 1'
    query_all = 'SELECT * FROM log  GROUP BY addr ORDER BY time DESC'
    
    def __init__(self, valve):
        Db.__init__(self)
        self.valve = valve
    
    def fetch(self):
        try:
            if self.valve != 'all':
                self.cursor.execute(self.query, (self.valve,))
            else:
                self.cursor.execute(self.query_all)
                
        except sqlite3.OperationalError:
            print("SQLite operational error. Database file invalid or not found")
            sys.exit(1);
            
        if self.valve != 'all':
            row = self.cursor.fetchone()
            if row is not None:
                return row
            else:
                return 'valve ' + str(self.valve) + 'not found'
        else:
            values = []
            for row in self.cursor:
                if row is not None:
                    res = []
                    res.append(str(row["addr"]))
                    res.append(str(self.getValveNameByAddr(str(row["addr"]))))
                    res.append(self.format(row))
                    values.append(' '.join(res))
                    
            return "\n".join(values)
        
    def __str__(self):
        value = self.fetch()
        self.close()
        if self.valve != "all":
            return self.format(value)
        else:
            return value
        
    def getValveNameByAddr(self, addr):
        for item in config.items('valves'):
            if str(item[1]) == str(addr):
                return item[0]
            
        return False
    