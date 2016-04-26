import random

from datetime import datetime
from jsonrpc import JSONRPCResponseManager, dispatcher

class TicTacToe:


    @staticmethod
    def getMove(gamestate):

        availableMoves = gamestate
        lookupIndex = 0

        for index in range(len(gamestate)):
            if gamestate[index] == "":
                availableMoves[index] = True
            else:
                availableMoves[index] = False

        for i in range(len(availableMoves)):
            if availablesMoves[index] == True and index % 2 == 0 and index != 4:        
                return i
            elif availablesMoves[index] == True:
                return i
        # for move in range(len(availableMoves)):
        #     randomIndex = random.randrange(len(availableMoves))
        #     if availableMoves[randomIndex] == True:
        #         return randomIndex


    @staticmethod
    def NextMove(gameid, mark, gamestate):

        move = TicTacToe.getMove(gamestate)

        returnMessage = {
            "position": move
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