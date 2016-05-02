import random

from datetime import datetime
from jsonrpc import JSONRPCResponseManager, dispatcher

class Tile(object):

    position = 0
    mark = ""

    def __init__(self, x, mark):
        self.position = x
        self.mark = ""

    def setMark(self, mark):
        self.mark = mark


class Board(object):

    length = 9


    def __init__(self):
        self.Board = [Tile(x, "") for x in range(self.length)]


    def findLegalMove(self):
        for i in range(self.length):
            if self.Board[i].mark == "":
                return i
            else:
                None


    def makeMove(self, mark):

        availablePlaces = 0

        if self.checkDefense(mark) is None:
            for i in range(self.length):
                if self.Board[i].mark == "":
                    return self.findLegalMove() 
        else:
            return self.checkDefense(mark)

    def checkDefense(self, mark):

        # check rows
        if self.Board[0].mark == self.Board[1].mark and self.Board[2].mark == "":
            return 2
        elif self.Board[1].mark == self.Board[2].mark and self.Board[0].mark == "":
            return 0
        elif self.Board[0].mark == self.Board[2].mark and self.Board[1].mark == "":
            return 1
        elif self.Board[3].mark == self.Board[4].mark and self.Board[5].mark == "":
            return 5
        elif self.Board[4].mark == self.Board[5].mark and self.Board[3].mark == "":
            return 3
        elif self.Board[3].mark == self.Board[5].mark and self.Board[4].mark == "":
            return 4
        elif self.Board[6].mark == self.Board[7].mark and self.Board[8].mark == "":
            return 8
        elif self.Board[7].mark == self.Board[8].mark and self.Board[6].mark == "":
            return 6
        elif self.Board[6].mark == self.Board[8].mark and self.Board[7].mark == "":
            return 7
        # check columns
        elif self.Board[0].mark == self.Board[3].mark and self.Board[6].mark == "":
            return 6
        elif self.Board[3].mark == self.Board[6].mark and self.Board[0].mark == "":
            return 0
        elif self.Board[0].mark == self.Board[6].mark and self.Board[3].mark == "":
            return 3
        elif self.Board[1].mark == self.Board[4].mark and self.Board[7].mark == "":
            return 7
        elif self.Board[4].mark == self.Board[7].mark and self.Board[1].mark == "":
            return 1
        elif self.Board[1].mark == self.Board[7].mark and self.Board[4].mark == "":
            return 4
        elif self.Board[2].mark == self.Board[5].mark and self.Board[8].mark == "":
            return 8
        elif self.Board[5].mark == self.Board[8].mark and self.Board[2].mark == "":
            return 2
        elif self.Board[2].mark == self.Board[8].mark and self.Board[5].mark == "":
            return 5
        # check diagonals
        elif self.Board[0].mark == self.Board[4].mark and self.Board[8].mark == "":
            return 8
        elif self.Board[4].mark == self.Board[8].mark and self.Board[0].mark == "":
            return 0
        elif self.Board[0].mark == self.Board[8].mark and self.Board[4].mark == "":
            return 4
        elif self.Board[2].mark == self.Board[4].mark and self.Board[6].mark == "":
            return 6
        elif self.Board[4].mark == self.Board[6].mark and self.Board[2].mark == "":
            return 2
        elif self.Board[2].mark == self.Board[6].mark and self.Board[4].mark == "":
            return 4
        else:
            return None


class TicTacToe(object):

    gameBoard = Board()

    def __init__(self, board):
        self.gameBoard = Board()
        count = 0
        for i in board:
            self.gameBoard.Board[count].setMark(i)
            count += 1


    @staticmethod
    def NextMove(gameid, mark, gamestate, opponent):

        t = TicTacToe(gamestate)

        position = t.gameBoard.makeMove(mark)
        returnMessage = {
            "position": position
        } 
        return returnMessage


    @staticmethod
    def Complete(gameid, winner, mark, gamestate):
        with open("logs/Game log.txt", "a") as win_file:
            win_file.write("ID: %s \nTime: %s \nWinner: %s \nBoard: %s \n" % (gameid, str(datetime.now()),winner, gamestate))
        return "OK"

    @staticmethod
    def Error(gameid, message, errorcode):
        print message
        return "OK"