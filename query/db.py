import sqlite3, sys
from config import configparser, config

class Db:

    conn = None
    file = None
    
    def __init__(self):
        self.getFile().connect().getCursor()
    
    def connect(self):
        self.conn = sqlite3.connect(self.file)
        return self

    def getFile(self):
        try:
            self.file = config.get("db", "file")
        except configparser.NoSectionError:
            print('Section "db" not found in configuration')
            sys.exit(1)
        except configparser.NoOptionError:
            print('Option "file" not found in configuration')
            sys.exit(1)
        
        return self
    
    def getCursor(self):
        self.cursor = self.conn.cursor()
        return self
    
    def close(self):
        self.conn.close()
        self.file = None
