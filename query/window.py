from query.simple import Simple

class Window(Simple):
    
    status = {
        0: "closed",
        1: "open"
    }
        
    def format(self, row):
        return self.status[row["window"]]

