# run by typing "python36 file-client.py {ip address} {text file}"

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

skt = socket.socket()
host = str(sys.argv[1])

if host == 'localhost': # resolve localhost to the name of localhost
    host = socket.gethostname()

port = 36650

try:
    skt.connect((host, port))
except socket.gaierror:
    print('ERROR: Invalid host')
    skt.close()
    quit()
except ConnectionRefusedError:
    print('ERROR: Connection was refused!  Is the server running?  Is the host-name correct?')
    skt.close()
    quit()
else:
    skt.send(dataToSend)
    recievedData = skt.recv(1024).decode('utf-8')
    
    print(recievedData)

    skt.close()

    dataFile.close()