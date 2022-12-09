class ScheduleChecker:
    conflict_count = 0
    contained_count = 0
    contiguous_count = 0
    
    def __init__(self):
        self.conflict_count = 0

    def getConflicts(self) -> int:
        return self.conflict_count

    def getContained(self) -> int:
        return self.contained_count

    def checkRange(self, ain:list[int], bin:list[int]):
        a_and_b = []
        a_xor_b = []
        a_and_b_test = []
        a = []
        b = []

        if ain.count(1) > bin.count(1):
            a = ain
            b = bin
        else:
            a = bin
            b = ain

        # calculate common bits
        for i in range(0, len(a)):
            a_and_b.append( (a[i] & b[i]) )

        # print (f"    a = {a}")
        # print (f"    b = {b}")
        # print (f"a & b = {a_and_b}")
        # print ("--------------------------------------")
        # print ("")

        # check contiguous (all bits zero)
        if a_and_b.count(0) == len(a_and_b):
            self.contiguous_count += 1
        else:
            # calculate xor bits
            for i in range(0, len(a)):
                a_xor_b.append( (a[i] ^ b[i]) )

            # print (f"    a = {a}")
            # print (f"    b = {b}")
            # print (f"a ^ b = {a_xor_b}")
            # print ("--------------------------------------")
            # print ("")

            # contains calc
            x_and_b_test = []
            for i in range(0, len(a)):
                x_and_b_test.append ( (a_xor_b[i] & b[i]) )

            # print (f"a ^ b = {a_xor_b}")
            # print (f"    b = {b}")
            # print (f" test = {x_and_b_test}")
            # print ("--------------------------------------")
            # print ("")

            contained = ( x_and_b_test.count(0) == len(x_and_b_test) )
            if (contained):
                self.contained_count += 1
            else:
                self.conflict_count += 1

checker = ScheduleChecker()
with open("input.txt", "r") as input:
    for line in input:
        # parse schedule pairs
        pairs = line.split(",")

        # parse upper and lower bounds of each schedule pair
        bounds = []
        bounds.append([int(x) for x in pairs[0].split('-')])
        bounds.append([int(x) for x in pairs[1].split('-')])

        # determine the mix/max values of schedule pairs
        flattened = [item for l in bounds for item in l]
        lower = min(flattened)
        upper = max(flattened)
        length = abs(lower-upper)

        # expand the pair min/max with range
        a_digits = range( bounds[0][0], bounds[0][1] + 1 )
        b_digits = range ( bounds[1][0], bounds[1][1] + 1 )

        # initialize the bitwise arrays to zero (off)
        a = [0] * (upper + 1)
        b = a.copy()

        # turn on bits for digits in the first schedule
        # Big(O) worry
        for d in a_digits:
            cur_digit = d
            cur_index = 0
            for e in a:
                if (d) == cur_index + 1:
                    a[cur_index] = 1
                cur_index += 1

        # turn on bits for digits in the second schedule
        # Big(O) worry
        for d in b_digits:
            cur_digit = d
            cur_index = 0
            for e in b:
                if (d) == cur_index + 1:
                    b[cur_index] = 1
                cur_index += 1

        checker.checkRange(a,b)

# First attempt (353) - too low
print (f"Answer={checker.getContained()}")