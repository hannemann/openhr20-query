from query.simple import Simple

class Mode(Simple):
        
    def format(self, row):
        return str(row["mode"])
