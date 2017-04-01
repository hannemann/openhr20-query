from query.mode import Mode
from query.valve import Valve
from query.real import Real
from query.wanted import Wanted
from query.battery import Battery
from query.error import Error
from query.window import Window
from query.connection import Connection
from query.format import Format


class Route:
    
    def __init__(self, query, valve, arg):
        
        if query == 'mode':
            print(Mode(valve))
            
        elif query == 'valve':
            print(Valve(valve))
            
        elif query == 'real':
            print(Real(valve))
            
        elif query == 'wanted':
            print(Wanted(valve))
            
        elif query == 'battery':
            print(Battery(valve))
            
        elif query == 'error':
            print(Error(valve))
            
        elif query == 'window':
            print(Window(valve))
            
        elif query == 'connection':
            print(Connection(valve))
            
        elif query == 'format':
            print(Format(valve, arg))
