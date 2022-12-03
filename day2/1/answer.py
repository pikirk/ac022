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
        # self.scores = [ [2,1,3], [8,4,2], [3,9,6] ] #7398
        self.scores = [ [4,1,7], [8,5,2], [3,9,6] ]   #10236

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

        if code == "AX":    #AA 4   TIE     ROCK PLAY ROCK
            rule = (0,0)
        elif code == "BX":  #BA 1   LOSS    ROCK PLAY PAPER 
            rule = (0,1)
        elif code == "CX":  #CA 7   WIN     ROCK PLAY SCISSORS
            rule = (0,2)    
        
        elif code == "AY":  #AB 8   WIN     PAPER PLAY ROCK
            rule = (1,0)
        elif code == "BY":  #BB 5   TIE     PAPER PLAY PAPER
            rule = (1,1)
        elif code == "CY":  #CB 2   LOSS    PAPER PLAY SCISSORS
            rule = (1,2)
        
        elif code == "AZ":  #CA 3   LOSS    SCISSOSRS PLAY ROCK
            rule = (2,0)
        elif code == "BZ":  #CB 9   WIN     SCISSORS PLAY PAPER
            rule = (2,1)
        elif code == "CZ":  #CC 6   TIE     SCISSORS PLAY SCISSORS
            rule = (2,2)
        else:
            raise Exception(f"No match. Code={code}")
        
        self.round_count += 1
        return self.scores[ rule[0] ] [ rule[1] ]

rps = Game()
line_count = 0
with open("input.txt", "r") as input:
    for line in input:
        line_count += 1
        rps.playRound(line[0], line[2])

print (f"Answer={rps.getScore()} | Lines={line_count} | Rounds={rps.getRoundCount()}") 
