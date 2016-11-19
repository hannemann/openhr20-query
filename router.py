from query.battery import Battery
from query.real import Real
from query.valve import Valve

class Route():
    
    def __init__(self, query, valve):
        
        if query == 'battery':
            print(Battery(valve))
        elif query == 'real':
            print(Real(valve))
        elif query == 'valve':
            print(Valve(valve))
