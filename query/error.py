from query.simple import Simple

class Error(Simple):
    
    errors = {
        0: "OK",
        1: "NA1",
        2: "NA2",
        4: "MONTAGE",
        8: "MOTOR",
        16: "RFM_SYNC",
        32: "NA5",
        64: "BAT_W",
        128: "BAT_E"
    }
        
    def format(self, row):
        return self.errors[row["error"]]

