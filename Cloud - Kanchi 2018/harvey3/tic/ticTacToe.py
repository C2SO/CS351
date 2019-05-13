#!/usr/bin/python3

# Author: Daniel Harvey

from enum import Enum

C_DEBUG = True


class Piece(Enum):
    NONE = 1
    X = 2
    O = 3


class PieceOutOfBoundsError(Exception):
    def __init__(self, message):
        self.message = message


class Point:
    Row = 0
    Col = 0

    def __init__(self, row, col):
        self.Row = row - 1
        self.Col = col - 1

    @staticmethod
    def NewPoint(point):
        return Point(point.Row + 1, point.Col + 1)

    def moveRight(self):
        self.Col += 1
        return self

    def moveLeft(self):
        self.Col -= 1
        return self

    def moveUp(self):
        self.Row += 1
        return self

    def moveDown(self):
        self.Row -= 1
        return self

    def moveUpRight(self):
        return self.moveUp().moveRight()

    def moveUpLeft(self):
        return self.moveUp().moveLeft()

    def moveDownLeft(self):
        return self.moveDown().moveLeft()

    def moveDownRight(self):
        return self.moveDown().moveRight()


class TicTacToe:
    winner = Piece.NONE
    board = None
    turn = Piece.NONE

    def __init__(self):
        self.winner = Piece.NONE
        self.board = Board()
        self.turn = Piece.X

    def playX(self, point):
        if self.turn == Piece.X:
            if not self.board.playX(point):
                return False, "This spot is taken already."

            if self.board.checkWin(point):
                self.winner = Piece.X
                return True, "X Wins!"

            self.turn = Piece.O
            return True, "X Team has placed their piece, O Team's turn now."
        else:
            # it's not your turn, X Team
            return False, "It's O Team's turn to place a piece."

    def playO(self, point):
        if self.turn == Piece.O:
            if not self.board.playO(point):
                return False, "This spot is taken already."

            if self.board.checkWin(point):
                self.winner = Piece.O
                return True, "O Wins!"

            self.turn = Piece.X
            return True, "O Team has placed their piece, X Team's turn now."
        else:
            # it's not your turn
            return False, "It's X Team's turn to place a piece."

    def displayBoard(self):
        return self.board.displayBoard()

    def testCheckWinDirectional(self):
        if C_DEBUG:
            print(self.board.checkWinDirectional(Point(3, 6), Point.moveRight, 'X', 0))

    def testCheckWin(self):
        self.board.checkWin(Point(3, 6))


class Board:
    BOARD_SIZE = None
    board = [[]]
    winCount = 0

    def __init__(self):
        self.BOARD_SIZE = 9
        self.winCount = 3
        self.board = [[None for i in range(self.BOARD_SIZE)] for j in range(self.BOARD_SIZE)]

    def playX(self, point):
        return self.playPiece(point, Piece.X)

    def playO(self, point):
        return self.playPiece(point, Piece.O)

    def playPiece(self, point, piece):
        self.pointBoundsCheck(point)

        if self.board[point.Row][point.Col] is None:
            pieceChar = None
            if piece == Piece.X:
                pieceChar = 'X'
            elif piece == Piece.O:
                pieceChar = '0'

            self.board[point.Row][point.Col] = pieceChar
            return True
        else:
            return False

    def displayBoard(self):
        returner = ''

        returner += "COL".center(5) + '\n'

        rnum = len(self.board)
        for row in self.board[::-1]:
            returner += str(rnum).center(5)

            for colItem in row:
                returner += ' '
                if colItem is None:
                    returner += '-'
                else:
                    returner += colItem
                returner += ' '

            returner += '\n'
            rnum -= 1
        else:
            returner += "ROW".center(5)
            for col in range(self.BOARD_SIZE):
                returner += str(col + 1).center(3)

        return returner

    def checkWin(self, point):
        """ Recursively search through the board in all possible lines to determine if the placement of piece at
            point has produced a winning configuration of pieces. """

        self.pointBoundsCheck(point)

        piece = self.board[point.Row][point.Col]
        if piece is None:
            return False

        piecesCount = self.checkWinDirectional(Point.NewPoint(point).moveRight(), Point.moveRight, piece, 0) \
                      + self.checkWinDirectional(Point.NewPoint(point).moveLeft(), Point.moveLeft, piece, 0) + 1

        if piecesCount >= self.winCount:
            if C_DEBUG:
                print("%d pieces in a row because of this move." % (piecesCount))
            return True

        piecesCount = self.checkWinDirectional(Point.NewPoint(point).moveUp(), Point.moveUp, piece, 0) \
                      + self.checkWinDirectional(Point.NewPoint(point).moveDown(), Point.moveDown, piece, 0) + 1

        if piecesCount >= self.winCount:
            if C_DEBUG:
                print("%s pieces in a row because of this move." % (piecesCount))
            return True

        piecesCount = self.checkWinDirectional(Point.NewPoint(point).moveUpRight(), Point.moveUpRight, piece, 0) \
                      + self.checkWinDirectional(Point.NewPoint(point).moveDownLeft(), Point.moveDownLeft, piece, 0) + 1

        if piecesCount >= self.winCount:
            if C_DEBUG:
                print("%s pieces in a row because of this move." % (piecesCount))
            return True

        piecesCount = self.checkWinDirectional(Point.NewPoint(point).moveDownRight(), Point.moveDownRight, piece, 0) \
                      + self.checkWinDirectional(Point.NewPoint(point).moveUpLeft(), Point.moveUpLeft, piece, 0) + 1

        if piecesCount >= self.winCount:
            if C_DEBUG:
                print("%s pieces in a row because of this move." % (piecesCount))
            return True
        else:  # all directions exhausted, no win
            if C_DEBUG:
                print("%s pieces in a row because of this move." % (piecesCount))
            return False

    def checkWinDirectional(self, point, moveFunc, piece, count):
        if count >= self.winCount - 1:
            return count
        else:
            if point.Row >= 0 and point.Col >= 0:
                try:
                    if self.board[point.Row][point.Col] == piece:
                        count += 1
                        moveFunc(point)
                        return self.checkWinDirectional(point, moveFunc, piece, count)
                    else:
                        return count
                except IndexError:
                    return count
            else:
                return count

    def pointBoundsCheck(self, point):
        if point.Row < 0 or point.Row >= self.BOARD_SIZE or point.Col < 0 or point.Col >= self.BOARD_SIZE:
            # out of bounds!
            raise PieceOutOfBoundsError("({},{}) is  not a valid position for a piece!"
                                        .format(point.Row + 1, point.Col + 1))


def boardTest():
    board = Board()
    print(board.displayBoard())
    board.playX(Point(1, 2))
    print(board.displayBoard())
    board.playO(Point(2, 2))
    print(board.displayBoard())


def testGame():
    game = TicTacToe()

    p1 = Point(1, 2)
    p2 = Point.NewPoint(p1)
    p1.moveRight()
    p2.moveLeft()
    print(game.playO(Point(3, 3)))
    print(game.playX(Point(3, 8)))
    print(game.playO(Point(2, 2)))
    print(game.playX(Point(3, 7)))
    print(game.playO(Point(2, 3)))
    print(game.playX(Point(3, 5)))
    print(game.playO(Point(6, 5)))
    print(game.playX(Point(3, 4)))
    print(game.playO(Point(6, 6)))
    print(game.playX(Point(3, 1)))
    print(game.displayBoard())
    print(game.playO(Point(5, 7)))
    print(game.playX(Point(3, 2)))
    print(game.playO(Point(7, 5)))
    print(game.displayBoard())

    # print(game.playX(Point(0,1))) # throws exception
    game.testCheckWin()



