from query.simple import Simple

class Real(Simple):
    
    query = 'SELECT real FROM log WHERE addr=? ORDER BY time DESC LIMIT 1'
        
    def format(self, value):
        return str(value/float(100))
