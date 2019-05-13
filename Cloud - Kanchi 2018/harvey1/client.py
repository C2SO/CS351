#!/usr/bin/python3

# Author: Daniel Harvey
# Written: April 11 2018

import sys, socket

try:
    fileName = str(sys.argv[2])
except IndexError:
    print("You did not provide a filename")
    quit()

try:
    dataFile = open(fileName,'r')
except FileNotFoundError:
    print("Could not open file \'" + fileName + '\'')
    quit()

dataToSend = dataFile.read().encode()

sck = socket.socket()
host = str(sys.argv[1])

if host == 'localhost': # resolve localhost to the name of localhost
    host = socket.gethostname()

port = 36650

try:
    sck.connect((host, port))
except socket.gaierror:
    print('ERROR: Invalid host')
    sck.close()
    quit()
except ConnectionRefusedError:
    print('ERROR: Connection was refused!  Is the server running?  Is the host-name correct?')
    sck.close()
    quit()
else:
    sck.send(dataToSend)
    recievedStuff = sck.recv(1024).decode('utf-8')
    
    print(recievedStuff)

    sck.close()

    dataFile.close()
