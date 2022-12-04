priority = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = priority.lower()
high_score = 0
low_score = 0
line_count = 1

with open("input.txt", "r") as input:
    for line in input:
        clean = line.replace("\n", "")
        mid = int(len(clean) / 2)
        front = set ( clean[:mid] )
        back = set ( clean[-mid:] )
        common = list (front & back)

        if len(common) == 1:
            hit = common[0]
            prioritize = hit in priority

            if prioritize:
                high_calc = ( (priority.index(hit)) + 27) 
                high_score += high_calc
                # print(f"Type={hit} | Score={high_calc} | Line={line_count}")
            else:
                low_calc =  (lower.index(hit)) + 1
                low_score += low_calc
                # print(f"Type={hit} | Score={low_calc} | Line={line_count}")
        else:
            print(f"----> Type={hit} | Line={clean} | Line={line_count}")
        
        line_count+=1

answer = high_score + low_score
print (f"Score={answer} | High={high_score} | Low={low_score}")


