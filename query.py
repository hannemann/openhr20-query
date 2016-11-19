#!/usr/bin/env python3

from config import configparser, config
from router import Route
import sys, getopt

def main(argv):

    valve = 0
    request = ''
    
    try:
        opts, args = getopt.getopt(argv, "v:br", ["valve="])
    except getopt.GetGetoptError:
        print("main.py -v <valve> -b")
        sys.exit(2)
        
    for opt, arg in opts:
        if opt in ("-v", "--valve"):
            try:
                valve = config.get("valves", arg)
            except configparser.NoSectionError:
                print('Section "valves" not found in configuration')
                sys.exit(1)
            except configparser.NoOptionError:
                print('Valve "' + arg + '" not found in configuration')
                sys.exit(1)
        elif opt == "-b":
            request = 'battery'
        elif opt == "-r":
            request = 'real'
    
    Route(request, valve)
        
if __name__ == "__main__":
    main(sys.argv[1:])