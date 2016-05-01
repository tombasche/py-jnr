import random

from datetime import datetime
from jsonrpc import JSONRPCResponseManager, dispatcher


class Move(object):
    side = None
    position = 0

    def __init__(self, side, position):
        self.side = side
        self.position = position


class Solver(object):
    pass


class Tile(object):

    position = 0
    mark = ""

    def __init__(self, x, mark):
        self.position = x
        self.mark = mark

    def setMark(self, mark):
        #print mark
        self.mark = mark


class Board(object):

    length = 9

    def __init__(self):
        self.Board = [Tile(x, "") for x in range(self.length)]


    def printBoard(self):
        for i in range(self.length):
            print self.Board[i].mark


class TicTacToe(object):

    gameBoard = Board()

    def __init__(self, board):
        self.gameBoard = Board()
        count = 0
        for i in board:
            self.gameBoard.Board[count].setMark(i)
            count += 1
            #self.gameBoard.getBoard()[count].setMark(i)


    @staticmethod
    def NextMove(gameid, mark, gamestate):

        t = TicTacToe(gamestate)
        t.gameBoard.printBoard()
        #print t.gameBoard.printBoard()

        # move = getMove(gamestate, mark)
        # print gameid
          
        # print 

        returnMessage = {
            "position": None
        } 
        return returnMessage


    @staticmethod
    def Complete(gameid, winner, mark, gamestate):
        with open("logs/Game log.txt", "a") as win_file:
            win_file.write("ID: %s \nTime: %s \nWinner: %s \nBoard: %s \n" % (gameid, str(datetime.now()),winner, gamestate))
        return "OK"

    @staticmethod
    def Error(gameid, message, errorcode):
        return "OK"