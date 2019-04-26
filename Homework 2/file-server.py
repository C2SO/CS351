#run by typing "python36 file-server.py"

import sys, socket

C_DEBUG = False

print("Initializing")

skt = socket.socket()
host = socket.gethostname()
port = 36650
skt.bind((host, port))

print("Listening...")

skt.listen(5)

while True:   
    conn, addr = skt.accept()
    
    print("Accepting connection from ", addr)

    data = conn.recv(1024).decode('utf-8')
    
    if C_DEBUG:
        print(data)

    # Parse the message to count the number of characters, words, and spaces
    numberOfChars = 0
    numberOfWords = 0
    numberOfLines = 0
    lastCharWhitespace = False

    for c in data :

        numberOfChars = numberOfChars + 1
        if c == ' ' :
            if not lastCharWhitespace:
                numberOfWords = numberOfWords + 1
            lastCharWhitespace = True
        elif c == '\n' :
            numberOfLines = numberOfLines + 1
            if not lastCharWhitespace:
                numberOfWords = numberOfWords + 1
            lastCharWhitespace = True
        else:
            lastCharWhitespace = False

        lastChar = c


    output = "Number of characters: %d\nNumber of words: %d\nNumber of lines: %d" \
        % (numberOfChars, numberOfWords, numberOfLines)
    
    print(output)

    conn.send(output.encode())

skt.close()