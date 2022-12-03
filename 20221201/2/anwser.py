cur_sum = 0
calcs = []

with open("input.txt", "r") as input:
    for line in input:
        if line.strip('\n') != '':
            cur_sum += int(line)
        else:
            calcs.append(cur_sum)
            cur_sum = 0

# case for single, eof file calc            
if cur_sum != 0:
    calcs.append(cur_sum)

calcs.sort()
answer = calcs.pop() + calcs.pop() + calcs.pop()
print (f"Answer={answer}")
