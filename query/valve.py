from query.simple import Simple

class Valve(Simple):
        
    def format(self, row):
        return str(row["valve"])
