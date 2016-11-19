from query.simple import Simple

class Battery(Simple):
            
    def format(self, row):
        return str(row["battery"]/float(1000))
