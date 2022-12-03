from array import *

class Game:
    scores = [[],[],[]]
    my_score = 0
    round_count = 0
    
    def __init__(self):
        self.initScoreMatrix()

    def initScoreMatrix(self):
        '''
        Holds the values of the scoring rules for the game
        Y axis (2nd element) represents the player
        X axis (1st element) represents the opponent
        '''
        self.scores = [ [3,1,2], [4,5,6], [8,9,7] ]

    def getScore(self):
        return self.my_score

    def getRoundCount(self):
        return self.round_count

    def playRound(self, opponentShape:str, playerShape:str):
        self.my_score += self.score( (opponentShape + playerShape) )

    def testRound(self,opponentShape:str, playerShape:str):
        return self.score( (opponentShape + playerShape) )

    def score(self, code:str) -> int:
        rule = ()
        # BUGBUG match/case not recognized in VS Code
        # X = Force loss
        # Y = Force draw
        # Z = force win

        if code == "AX":    #AC 3   FL      SCISSORS LOSES TO ROCK
            rule = (0,0)
        elif code == "BX":  #BA 1   FL      ROCK LOSES TO PAPER
            rule = (0,1)
        elif code == "CX":  #CA 2   FL      PAPER LOSES TO SCISSORS
            rule = (0,2)    
        
        elif code == "AY":  #AA 4   FD      ROCK DRAWS ROCK
            rule = (1,0)
        elif code == "BY":  #BB 5   FD      PAPER DRAWS PAPER
            rule = (1,1)
        elif code == "CY":  #CC 6   FD      SCISSORS DRAWS SCISSORS
            rule = (1,2)
        
        elif code == "AZ":  #AC 8   FW      PAPER BEATS ROCK
            rule = (2,0)
        elif code == "BZ":  #BC 9   FW      SCISSORS BEAT PAPER
            rule = (2,1)
        elif code == "CZ":  #CA 7   FW      ROCK BEATS SCISSORS
            rule = (2,2)
        else:
            raise Exception(f"No match. Code={code}")
        
        self.round_count += 1
        return self.scores[ rule[0] ] [ rule[1] ]


'''
A Y
B X
C Z
'''
rps = Game()
rps.playRound("A","Y")
rps.playRound("B","X")
rps.playRound("C","Z")
print (f"Answer={rps.getScore()}")

rps = Game()
line_count = 0
with open("input.txt", "r") as input:
    for line in input:
        line_count += 1
        rps.playRound(line[0], line[2])

# Attempt 1: 11630 (too low)
print (f"Answer={rps.getScore()} | Lines={line_count} | Rounds={rps.getRoundCount()}") 
