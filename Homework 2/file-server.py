import sys, socket

C_DEBUG = False

print("Initializing")

sck = socket.socket()
host = socket.gethostname()
port = 36650
sck.bind((host, port))

print("Listening...")

sck.listen(5)

while True:   
    conn, addr = sck.accept()
    
    print("Accepting connection from ", addr)

    data = conn.recv(1024).decode('utf-8')
    
    print(data)

    # Parse the message to count the number of characters, words, and spaces
    numberOfChars = 0
    numberOfWords = 0
    numberOfLines = 0
    lastCharWasWhitespace = False

    for c in data :

        numberOfChars = numberOfChars + 1
        if c == ' ' :
            if not lastCharWasWhitespace:
                numberOfWords = numberOfWords + 1
                #print(lastChar)
            lastCharWasWhitespace = True
        elif c == '\n' :
            numberOfLines = numberOfLines + 1
            if not lastCharWasWhitespace:
                numberOfWords = numberOfWords + 1
                #print(lastChar)
            lastCharWasWhitespace = True
        else:
            lastCharWasWhitespace = False

        lastChar = c


    processedInput = "Number of characters: %d\nNumber of words: %d\nNumber of lines: %d" \
        % (numberOfChars, numberOfWords, numberOfLines)
    
    if C_DEBUG:
        print(processedInput)

    # Return the business to the client
    conn.send(processedInput.encode())

    if C_DEBUG:
        print()

sck.close()