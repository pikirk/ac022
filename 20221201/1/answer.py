cur = 0
cur_sum = 0
answer = 0

with open("input.txt", "r") as input:
    for line in input:
        if line.strip('\n') != '':
            cur_sum += int(line)
        else:
            if cur_sum > answer:
                answer = cur_sum
            cur_sum = 0

print (f"Answer={answer}")