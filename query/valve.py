from query.simple import Simple

class Valve(Simple):
    
    query = 'SELECT valve FROM log WHERE addr=? ORDER BY time DESC LIMIT 1'
        
#    def format(self, value):
#        return str(value/float(100))
