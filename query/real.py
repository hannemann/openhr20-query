from query.simple import Simple

class Real(Simple):
    
    query = 'SELECT real FROM log WHERE addr=? ORDER BY id LIMIT 1'
        
    def format(self, value):
        return str(value/float(100))
