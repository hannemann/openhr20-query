from query.simple import Simple

class Wanted(Simple):
        
    def format(self, row):
        return str(row["wanted"]/float(100))
