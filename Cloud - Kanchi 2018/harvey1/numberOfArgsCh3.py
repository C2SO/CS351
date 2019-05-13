#!/usr/bin/python

# Author: Daniel Harvey
# Written: April 9 2018

import sys

argCount = len(sys.argv) - 1 # subtract one to account for the first "argument", the program name

print("There are " + str(argCount) + " arguments."); 

if argCount >=3 :
    print("There are 3 or more arguments")
else:
    print("There are less than 3 arguments")


