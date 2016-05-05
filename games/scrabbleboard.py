letterScore = {
    'A' : 1,
    'B' : 3,
    'C' : 3,
    'D' : 2,
    'E' : 1,
    'F' : 4,
    'G' : 2,
    'H' : 4,
    'I' : 1,
    'J' : 8,
    'K' : 5,
    'L' : 1,
    'M' : 3,
    'N' : 1,
    'O' : 1,
    'P' : 3,
    'Q' : 10,
    'R' : 1,
    'S' : 1,
    'T' : 1,
    'U' : 1,
    'V' : 4,
    'W' : 4,
    'X' : 8,
    'Y' : 4,
    'Z' : 10
}


class ScrabblePiece(object):

    attribute = "."
    x = 0
    y = 0
    letter = "A"
    owned = False

    def __init__(self,x,y):
        self.x = x
        self.y =y

        # if self.x == 0 and self.y == 0:
        #     self.attribute = "3xW"

        # elif self.x == self.y:
        #     self.attribute = "2xW"



class ScrabbleBoard(object):

    w, h = 15, 15 
    Board = None

    def __init__(self):  
        self.Board = [[ScrabblePiece(x,y) for x in range(self.w)] for y in range(self.h)] 

    def PrintBoard(self):
        for i in range(self.w):
            for j in range(self.h):
                print str(self.Board[i][j].attribute)
        self.CalculateScore()

    def CalculateScore(self):
        totalScore = 0
        for i in range(self.w):
            for j in range(self.h):
                if self.Board[i][j].letter is not None and self.Board[i][j].owned is True:
                    totalScore += letterScore[self.Board[i][j].letter]
        print totalScore

    

    # def CheckPieceScore(self, i, j):
    #     if self.board[i][j] = True:
    #         if self.board[i]