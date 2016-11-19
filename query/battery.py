from query.simple import Simple

class Battery(Simple):
    
    query = 'SELECT battery FROM log WHERE addr=? ORDER BY id LIMIT 1'
        
    def format(self, value):
        return str(value/float(1000))
