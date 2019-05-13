#!/usr/bin/python3

# Author: Daniel Harvey
# Written: April 26 2018

import xmlrpc.client, socket

dataFilePath = 'calculate.txt'

def processData(fileName, adder, multiplier):
    output = ""
    try:
        opText = open(fileName,'r').read()
           
        for line in opText.split('\n'):
            operation = line.split()
            if len(operation) == 3:
                if operation[0] == 'A':
                    output+= adder.add(str(operation[1]), str(operation[2])) + '\n'
                elif operation[0] == 'M':
                    output += multiplier.multiply(str(operation[1]), str(operation[2])) + '\n'

    except FileNotFoundError:
        output = "Could not open file \'" + dictFileName + '\''
        
    return output.strip()

adderHostname = socket.gethostname()
multiplierHostname = socket.gethostname()
addServer = xmlrpc.client.ServerProxy('http://' + adderHostname + ':8000')
multServer = xmlrpc.client.ServerProxy('http://' + multiplierHostname + ':8001')

#print(addServer.add('1','9999'))
#print(multServer.multiply('101','9999'))

results = processData(dataFilePath, addServer, multServer)

print(results)
