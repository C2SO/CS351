#!/usr/bin/python3

# Author: Daniel Harvey
# Written: June 4 2018

import sys, socket, json

C_DEBUG = True

sck = socket.socket()
host = socket.gethostname()
port = 9000
sck.bind((host, port))
PEER_LIST = []

sck.listen(5)

server_fd, server_ip, server_port = None, None, None

# TODO, eventually make this whole program work for more than two peers.  
# not necessary for the assignment though

# Set up the "leader" peer, which is the first to connect
while server_fd is None:
    server_fd, server_ip = sck.accept()
else:
    PEER_LIST.append(server_fd)  # TODO maybe make this also hold the IPs
    server_fd.send('SERVER'.encode())
    server_port = int(server_fd.recv(1024).decode('utf-8'))
    if C_DEBUG:
        print("Accepting peer server connection from ", server_ip)

# Handle redirection of any subsequent peer connection to the leader peer
while server_fd is not None and len(PEER_LIST) > 0:
    conn, addr = sck.accept()
    conn.send('CLIENT'.encode())
    PEER_LIST.append(conn)

    if C_DEBUG:
        print("Accepting peer client connection from ", addr)
    conn.recv(1024)  # dummy just to make sure message are kept in order

    # serialize the connection info to send to the new peer
    conn.send(json.dumps((server_ip, server_port)).encode())

sck.close()
