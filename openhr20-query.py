#!/usr/bin/env python3

from config import configparser, config
from router import Route
import sys, getopt

def usage():
    print()
    print("Retrieve info from openhr20 database")
    print()
    print("\tquery.py -d <device_name> -mvrwbeof")
    print()
    print("\t--device\t-d The device you want to query")
    print("\t\t\t-h Print this help screen")
    print("\t\t\t-m Mode")
    print("\t\t\t-v Valve position")
    print("\t\t\t-r Real temperature")
    print("\t\t\t-w Wanted temperature")
    print("\t\t\t-b Battery status")
    print("\t\t\t-e Error number")
    print("\t\t\t-o Window open/closed")
    print("\t\t\t-c Connection status")
    print("\t--format\t-f format string")
    print("\t\t\t   e.g.: Real Temperature: %rC")
    print()
    

def main(argv):

    valve = 0
    request = ''
    
    try:
        opts, args = getopt.getopt(argv, "d:f:hmvrwbeoc", ["device=", "format="])
    except getopt.GetoptError as e:
        print()
        print("Error: " + str(e))
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            usage()
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
        elif opt == "-f":
            request = 'format'
    
    Route(request, valve, arg)
        
if __name__ == "__main__":
    main(sys.argv[1:])
