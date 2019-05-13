#!/usr/bin/python3

import sys
import re
import socket
import select
import ticTacToe

C_DEBUG = True

HOST = ''
SOCKET_LIST = []
X_PLAYER_LIST = []
O_PLAYER_LIST = []
RECV_BUFFER = 4096
PORT = 9009


def tic_tac_toe_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)

    nextPieceToJoin = ticTacToe.Piece.X

    game = ticTacToe.TicTacToe()

    print("Tic Tac Toe server started on port " + str(PORT))

    while game.winner == ticTacToe.Piece.NONE:

        # get the list sockets which are ready to be read through select
        # 4th arg, time_out  = 0 : poll and never block
        ready_to_read, ready_to_write, in_error = select.select(SOCKET_LIST, [], [], 0)

        for sock in ready_to_read:
            # a new connection request received
            if sock == server_socket:
                sockfd, addr = server_socket.accept()

                SOCKET_LIST.append(sockfd)

                print("Client (%s, %s) connected" % addr)
                broadcast(server_socket, "[{}:{}] entered our game, joining {} team"
                          .format(addr[0], addr[1], str(nextPieceToJoin).split('.')[1]))

                if nextPieceToJoin == ticTacToe.Piece.X:
                    X_PLAYER_LIST.append(sockfd)
                    nextPieceToJoin = ticTacToe.Piece.O
                elif nextPieceToJoin == ticTacToe.Piece.O:
                    O_PLAYER_LIST.append(sockfd)
                    nextPieceToJoin = ticTacToe.Piece.X

                if C_DEBUG:
                    print("X Team:")
                    print(X_PLAYER_LIST)
                    print("\nO Team:")
                    print(O_PLAYER_LIST)

            # a message from a client, not a new connection
            else:
                # process data received from client
                try:
                    # receiving data from the socket.
                    data = sock.recv(RECV_BUFFER)

                    if data:
                        if game.turn == ticTacToe.Piece.X and sock in X_PLAYER_LIST or \
                          game.turn == ticTacToe.Piece.O and sock in O_PLAYER_LIST:
                            # there is something in the socket, check if it is from valid
                            data = data.decode('utf-8')

                            # process the data to see if the input is a valid position
                            match = re.search(r"\((\d+),(\d+)\)", str(data))
                            if match:
                                pos = ticTacToe.Point(int(match.group(1)), int(match.group(2)))

                                success = False
                                message = ''

                                # play piece
                                if game.turn == ticTacToe.Piece.X:
                                    success, message = game.playX(pos)
                                elif game.turn == ticTacToe.Piece.O:
                                    success, message = game.playO(pos)

                                if not success:
                                    team_list = getTeamList(sock)
                                    broadcast_team(server_socket, team_list, message)
                                else:
                                    message += '\n' + game.displayBoard()
                                    broadcast(server_socket, message)

                            else:  # invalid position
                                broadcast_one(server_socket, sock, "That is not a valid position. "
                                                                   "Enter \"(row,col)\" to play a piece.")

                        else:
                            team_list = getTeamList(sock)
                            broadcast_team(server_socket, team_list,
                                           "It's not your team's turn to place a piece.")
                    else:
                        # remove the socket that's broken
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)

                            if sock in X_PLAYER_LIST:
                                X_PLAYER_LIST.remove(sock)
                            elif sock in O_PLAYER_LIST:
                                O_PLAYER_LIST.remove(sock)

                        # at this stage, no data means probably the connection has been broken
                        broadcast(server_socket, "Client (%s, %s) is offline" % addr)

                        #  check if there are still enough players; if not, end the game
                        if len(X_PLAYER_LIST) < 1 or len(O_PLAYER_LIST) < 1:
                            broadcast(server_socket, "Other team has left completely, ending game")

                            #  set the winner to escape the loop
                            if len(O_PLAYER_LIST) > 0:
                                game.winner = ticTacToe.Piece.X
                            else:
                                game.winner = ticTacToe.Piece.O

                            break

                # exception
                except ticTacToe.PieceOutOfBoundsError as ex:
                    broadcast_one(server_socket, sock, "That piece is out of bounds.  Try again.")
                except Exception as ex:
                    broadcast(server_socket, "Client (%s, %s) is offline" % addr)
                    continue

    else:
        server_socket.close()


def getTeamList(sock):
    if sock in X_PLAYER_LIST:
        team_list = X_PLAYER_LIST
    elif sock in O_PLAYER_LIST:
        team_list = O_PLAYER_LIST
    else:
        team_list = []

    return team_list


# broadcast chat messages to all connected clients
def broadcast(server_socket, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        if socket != server_socket:
            try:
                socket.send(('\r' + message + '\n').encode())
            except Exception as ex:
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)

                    if socket in X_PLAYER_LIST:
                        X_PLAYER_LIST.remove(socket)
                    elif socket in O_PLAYER_LIST:
                        O_PLAYER_LIST.remove(socket)

    if C_DEBUG:
        print(message)


# broadcast messages to one client
def broadcast_one(server_socket, sock, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        if socket == sock:
            try:
                socket.send(('\r' + message + '\n').encode())
            except Exception as ex:
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)

                    if socket in X_PLAYER_LIST:
                        X_PLAYER_LIST.remove(socket)
                    elif socket in O_PLAYER_LIST:
                        O_PLAYER_LIST.remove(socket)

    if C_DEBUG:
        print(message)


# broadcast messages to one team
def broadcast_team(server_socket, team_list, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        if socket != server_socket and socket in team_list:
            try:
                socket.send(('\r' + message + '\n').encode())
            except Exception as ex:
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)

                    if socket in X_PLAYER_LIST:
                        X_PLAYER_LIST.remove(socket)
                    elif socket in O_PLAYER_LIST:
                        O_PLAYER_LIST.remove(socket)

    if C_DEBUG:
        print(message)


if __name__ == "__main__":
    sys.exit(tic_tac_toe_server())
