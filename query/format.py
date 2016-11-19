import re
from query.simple import Simple
from query.mode import Mode
from query.valve import Valve
from query.real import Real
from query.wanted import Wanted
from query.battery import Battery
from query.error import Error
from query.window import Window
from query.connection import Connection

class Format(Simple):
    
    obj = {
        "m": Mode,
        "v": Valve,
        "r": Real,
        "w": Wanted,
        "b": Battery,
        "e": Error,
        "o": Window,
        "c": Connection,
    }
    regex = re.compile("%([a-z])")
    
    def __init__(self, valve, arg):
        Simple.__init__(self, valve)
        self.arg = arg
        
    def format(self, row):
        
        self.row = row
        format = self.arg
        res = self.regex.findall(format)
        
        if res is not None:
            for q in res:
                format = format.replace("%" + q, self.getFormattedValue(q))
        
        return format
    
    def getFormattedValue(self, q):
        
        obj = self.obj[q]
        return obj.format(obj(self.valve), self.row)