from query.simple import Simple

class Real(Simple):
        
    def format(self, row):
        return str(row["real"]/float(100))
