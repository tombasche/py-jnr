import random

from datetime import datetime
from jsonrpc import JSONRPCResponseManager, dispatcher

from scrabbleboard import ScrabbleBoard

class Scrabble(object):

    board = ScrabbleBoard()

    # use to test for now
    @staticmethod
    def Ping():
        Scrabble.board.PrintBoard()
        pass

    @staticmethod
    def Error(gameid, message, errorcode):
        return "OK"
