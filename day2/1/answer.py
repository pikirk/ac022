from array import *

class Game:
    scores = [[],[],[]]
    my_score = 0
    
    def __init__(self):
        self.initScoreMatrix()

    def initScoreMatrix(self):
        '''
        Holds the values of the scoring rules for the game
        Y axis (2nd element) represents the player
        X axis (1st element) represents the opponent
        '''
        #self.scores = [ ["1","1","3"], ["8","2","2"], ["3","9","3"] ]
        self.scores = [ [2,1,3], [8,4,2], [3,9,6] ]

    def getScore(self):
        return self.my_score

    def playRound(self, opponentShape:str, playerShape:str):
        self.my_score += self.score( (opponentShape + playerShape) )

    def score(self, code:str) -> int:
        rule = ()
        # BUGBUG match not recognized in VS Code
        # match code:
        #     case "AX":
        #         rule = (0,0)
        #     case "AY":
        #         rule = (1,0)
        #     case "AZ":
        #         rule = (2,0)
        #     case "BX":
        #         rule = (0,1)
        #     case "BY":
        #         rule = (1,1)
        #     case "BZ":
        #         rule = (1,2)
        #     case "CX":
        #         rule = (0,2)
        #     case "CY":
        #         rule = (1,2)
        #     case "CZ":
        #         rule = (2,2)

        if code == "AX":    #AA
            rule = (0,0)
        elif code == "AY":  #AB
            rule = (1,0)
        elif code == "AZ":  #AC
            rule = (2,0)
        elif code == "BX":  #BA
            rule = (0,1)
        elif code == "BY":  #BY
            rule = (1,1)
        elif code == "BZ":  #BZ
            rule = (1,2)
        elif code == "CX":  #CA
            rule = (0,2)
        elif code == "CY":  #CB
            rule = (1,2)
        elif code == "CZ":  #CC
            rule = (2,2)
        else:
            print (f"No match. Code={code}")

        val = self.scores[ rule[0] ] [ rule[1] ]
        print (f"Code={code} | Rule={rule} | Score={val}" )
        return val


'''
Sample input
A Y
B X
C Z
'''
rps = Game()
rps.playRound("A", "Y")
rps.playRound("B", "X")
rps.playRound("C", "Z")

print (f"Answer={rps.getScore()}")

