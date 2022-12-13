class MoveSequence:
    count = 0
    _from = 0
    _to = 0
    empty = "   "
    
    def __init__(self, raw:list[int]):
        self.count = raw[0]
        self._from = raw[1]
        self._to = raw[2]

    def getCount(self) -> int:
        return self.count

    def getFrom(self) -> int:
        return self._from
    
    def getTo(self) -> int:
        return self._to

    def execute(self, matrix:list[list]):
        crates = self.configureFrom(matrix)
        self.configureTo(crates, matrix)

        # clean
        if (matrix[0].count(self.empty) == len(matrix[0])):
            matrix.pop(0)

    def configureTo(self, crates:list[str], matrix:list[list]):
        height = len(matrix)
        stack = matrix[height-1][self._to - 1]

        # add sourced crates to target
        for i in range(0, len(crates) ):
            # find first available slot, if any, in the target
            crate = crates.pop(0)
            slot = False
            for s in range(len(matrix), 0, -1):
                slot = matrix[s - 1][self._to - 1] == self.empty
                if slot:
                    matrix[s - 1][self._to -1] = crate 
                    break;

            # add new row
            if not slot:
                newrow = [self.empty] * len(matrix[0])
                newrow[(self._to - 1)] = crate
                matrix.insert(0, newrow)

    def configureFrom(self, matrix:list[list]) -> list[str]:
        height = len(matrix)
        crates = []
        stack = matrix[height - 1][self._from - 1]

        # get the top most crate
        counter = 0
        for item in range( 0, self.count ):
            for row  in range (0, height ):
                crate = matrix[row][self._from - 1]

                if crate != self.empty:
                    matrix[row][self._from - 1] = self.empty # swap the item with empty
                    crates.append(crate)
                    counter += 1
                    break;
        return crates

matrix = []
sequenceList = []
instructionsFlag = False
with open("input.txt", "r") as input:
    for line in input:
        if (len(line) == 1):
            instructionsFlag = True
        elif not instructionsFlag:
            clean = line.strip('\n')
            matrix.append( [clean[0:3], clean[4:7], clean[8:11], clean[12:15], clean[16:19], clean[20:23], clean[24:27], clean[28:31], clean[32:35]] ) 

        if (instructionsFlag and len(line) > 1):
            pad = 1 if len(line[5:7].strip()) == 2 else 0
            raw = [ int(line[5:7].strip()), int(line[12+pad:13+pad].strip()), int(line[17+pad:18+pad].strip()) ]
            sequenceList.append( MoveSequence(raw) )

# stack label not needed
matrix.pop(-1)
for s in range (0, len(sequenceList)):
    seq = sequenceList.pop(0)
    seq.execute(matrix)

