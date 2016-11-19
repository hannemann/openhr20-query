from query.simple import Simple
from time import time

class Connection(Simple):
    
    threshold = {
        "warning": 480,
        "error": 1200
    }
        
    def format(self, row):
        
        last = row["time"]
        
        if int(time()-last) > self.threshold["error"]:
            return "error"
        elif int(time()-last) > self.threshold["warning"]:
            return "warning"
        else:
            return "OK"

