#!/usr/bin/python3

# Author: Daniel Harvey
# Written: June 4 2018

import os
import sys
import socket
import re
import json

C_DEBUG = False


def sanitize(word):
    return _right_sanitize(word.lower())


def _right_sanitize(word):
    if len(word) > 0 and not (word[-1]).isalnum():
        return _right_sanitize(word[:-1])
    else:
        return _left_sanitize(word)


def _left_sanitize(word):
    if len(word) > 0 and not word[0].isalnum():
        return _left_sanitize(word[1:])
    else:
        return word


def build_dictionary(data):
    word_counts = {}

    # count all of the words
    for superword in data.split():
        for word in superword.split("—"):
            word = sanitize(word)
            if len(word) >= 5:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts.update({str(word): 1})

    # now pick the top 50
    top_50_words = sorted(word_counts, key=lambda key: word_counts[key], reverse=True)

    top_word_counts = {}
    for i in range(50):
        top_word_counts.update({top_50_words[i]: word_counts[top_50_words[i]]})
    return top_word_counts


# ------------------------- #
#       MAIN CODE           #
# ------------------------- #

try:
    URL = str(sys.argv[2])
except IndexError:
    print("You did not provide a book URL or a torrent gateway address")
    quit()

try:
    os.system('wget ' + URL)
    file_name = re.fullmatch(r"^.+\/(.+)$", URL).group(1)
    e_book = open(file_name, 'r', encoding="utf-8").read()
    os.system('rm ' + file_name)
except Exception as ex:
    print(str(ex) + "Could not fetch or open file \'" + file_name + '\'')
    quit()

# Build the local dictionary of word frequencies
local_word_counts = build_dictionary(e_book)

# Connect to torrent gate
sck = socket.socket()
host = str(sys.argv[1])

if host == 'localhost':  # resolve localhost to the name of localhost
    host = socket.gethostname()

port = 9000

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
else:  # torrent gate connection successful, begin communication

    peer_word_counts = {}

    # We should receive what role we are from the torrent gate
    role = sck.recv(1024).decode('utf-8')

    if role == 'SERVER':
        listener = socket.socket()
        listener_host = socket.gethostname()
        listener_port = 9009
        listener.bind((listener_host, listener_port))

        # send the torrent gate back my listener port number
        sck.send(str(listener_port).encode())

        listener.listen(5)

        client_fd, client_ip = listener.accept()

        if C_DEBUG:
            print(client_ip)

        peer_word_counts = json.loads(client_fd.recv(1024).decode('utf-8'))
        client_fd.send(json.dumps(local_word_counts).encode())

    elif role == 'CLIENT':
        peer = socket.socket()
        sck.send(b'1')  # dummy message to make sure messages are read correctly
        peer_host = json.loads(sck.recv(1024).decode('utf-8'))

        if C_DEBUG:
            print(peer_host)

        peer_host_name, peer_host_port = socket.gethostbyaddr(peer_host[0][0])[0], peer_host[1]

        if peer_host_name == 'localhost':  # resolve localhost to the name of localhost
            peer_host_name = socket.gethostname()

        if C_DEBUG:
            print(peer_host_name, peer_host_port)

        peer.connect((peer_host_name, peer_host_port))
        peer.send(json.dumps(local_word_counts).encode())
        peer_word_counts = json.loads(peer.recv(1024).decode('utf-8'))

        peer.close()


    if C_DEBUG:
        print(local_word_counts)
        print(peer_word_counts)

    # Intersect the word counts and display results
    intersected_words = [word for word in local_word_counts if word in peer_word_counts]
    for word in intersected_words:
        print('%20s: %7d' % (word, local_word_counts[word] + peer_word_counts[word]))

    sck.close()
