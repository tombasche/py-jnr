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
    playerMark = ""
    opponentMark = ""

    def __init__(self, mark):
        self.Board = [Tile(x, "") for x in range(self.length)]
        self.playerMark = mark
        if self.playerMark == "X":
            self.opponentMark = "O"
        else:
            self.opponentMark = "X"

    def printBoard(self):
        for i in range(self.length):
            print self.Board[i].mark


    def score(self):
        if self.checkWin(self.playerMark):
            return 10
        elif self.checkWin(self.opponentMark):
            return -10
        else:
            return 0


    def findLegalMove(self):


        print "finding legal move..."
        for i in range(self.length):
            if self.Board[i].mark == "":             
                self.printBoard()
                print self.score()
                if self.score() == 10:
                    return i
                elif self.score() == 0:
                    return i
                else:
                    self.findLegalMove()
            else:
                None


    def checkWin(self, mark):

        # check rows
        if self.Board[0].mark == self.Board[1].mark == self.Board[2].mark:
            return True
        elif self.Board[3].mark == self.Board[4].mark == self.Board[5].mark:
            return True
        elif self.Board[6].mark == self.Board[7].mark == self.Board[8].mark:
            return True
        # check columns
        elif self.Board[0].mark == self.Board[3].mark == self.Board[6].mark:
            return True
        elif self.Board[1].mark == self.Board[4].mark == self.Board[7].mark:
            return True
        elif self.Board[2].mark == self.Board[5].mark == self.Board[8].mark:
            return True
        # check diagonals
        elif self.Board[0].mark == self.Board[4].mark == self.Board[8].mark:
            return True
        elif self.Board[2].mark == self.Board[4].mark == self.Board[6].mark:
            return True
        else:
            return None


class TicTacToe(object):

    gameBoard = Board("")

    def __init__(self, board, mark):
        self.gameBoard = Board(mark)
        count = 0
        for i in board:
            self.gameBoard.Board[count].setMark(i)
            count += 1


    @staticmethod
    def NextMove(gameid, mark, gamestate, opponent):

        t = TicTacToe(gamestate, mark)
        position = t.gameBoard.findLegalMove()
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