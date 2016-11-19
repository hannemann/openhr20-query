#!/usr/bin/env python3

from config import configparser, config
from router import Route
import sys, getopt

def printHelp():
    print()
    print("Retrieve info from openhr20 database")
    print()
    print("\tquery.py -d <device_name> -mvrwbeof")
    print()
    print("\t\t-h\t\tPrint this help screen")
    print("\t\t-m\t\tMode")
    print("\t\t-v\t\tValve position")
    print("\t\t-r\t\tReal temperature")
    print("\t\t-w\t\tWanted temperature")
    print("\t\t-b\t\tBattery status")
    print("\t\t-e\t\tError number")
    print("\t\t-o\t\tWindow open/closed")
    print("\t\t-c\t\tConnection status")
    print("\t\t-f\t\tformat string")
    print("\t\t\t\te.g.: Real Temperature: %r°")
    print()
    

def main(argv):

    valve = 0
    request = ''
    
    try:
        opts, args = getopt.getopt(argv, "d:hmvrwbeocf", ["device="])
    except getopt.GetoptError as e:
        print()
        print("Error: " + str(e))
        printHelp()
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == "-h":
            printHelp()
            sys.exit(0)
        elif opt in ("-d", "--device"):
            try:
                valve = config.get("valves", arg)
            except configparser.NoSectionError:
                print('Section "valves" not found in configuration')
                sys.exit(1)
            except configparser.NoOptionError:
                print('Valve "' + arg + '" not found in configuration')
                sys.exit(1)
        elif opt == "-m":
            request = 'mode'
        elif opt == "-v":
            request = 'valve'
        elif opt == "-r":
            request = 'real'
        elif opt == "-w":
            request = 'wanted'
        elif opt == "-b":
            request = 'battery'
        elif opt == "-e":
            request = 'error'
        elif opt == "-o":
            request = 'window'
        elif opt == "-c":
            request = 'connection'
    
    Route(request, valve)
        
if __name__ == "__main__":
    main(sys.argv[1:])
