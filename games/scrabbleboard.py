

class ScrabblePiece(object):

    attribute = "."

    def __init__(self,x,y):
        if x == 0 and y == 0:
            self.attribute = "3xW"

        elif x == y and x is not 0 and y is not 0:
            self.attribute = "2xW"



class ScrabbleBoard(object):

    w, h = 15, 15 
    Board = None

    def __init__(self):  
        self.Board = [[ScrabblePiece(x,y) for x in range(self.w)] for y in range(self.h)] 

    # def PrintBoard(self):
    #     for i in range(self.w):
    #         for j in range(self.h):
    #             print self.Board[i][j].attribute


    def CalculateScore(self):
        for i in range(self.w):
            for j in range(self.h):
                if self.board[i][j] == True:
                    pass

    # def CheckPieceScore(self, i, j):
    #     if self.board[i][j] = True:
    #         if self.board[i]