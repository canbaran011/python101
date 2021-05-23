#!/bin/python3

import sys
import socket
from datetime import datetime

#python3 scanner.py <ip>

#define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate a hostname to IP4
else:
    print("Invalid amount of arguments")    
    print("Syntax : python3 scanner.py <ip>")
    sys.exit()    

#python3 scanner.py 192 --on terminal

#Add pretty banner
print("-" * 50)
print("scanning target " + target)
print("Time started " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) #is a float
        result = s.connect_ex((target,port)) #returns errot indicator
        print("Checking port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\nExitting program")
    sys.exit()

except socket.gaierror:
    print("hostname could not be resolved")
    sys.exit()
except socket.error:
    print("could not connect to server")
    sys.exit()






