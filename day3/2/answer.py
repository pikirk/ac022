priority = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = priority.lower()
high_score = 0
low_score = 0
line_count = 1
group_counter = 1
group = []

with open("input.txt", "r") as input:
    for line in input:
        clean = line.replace("\n", "")

        # gather group items
        if group_counter <= 3:
            group.append(clean)
        
        # eval group score
        if group_counter == 3:
            first = set ( group[0] )
            second = set ( group[1] )
            third = set ( group[2] )
            common = list (first & second & third)
            
            if len(common) == 1:
                hit = common[0]
                prioritize = hit in priority

                if prioritize:
                    high_calc = ( (priority.index(hit)) + 27) 
                    high_score += high_calc
                    print(f"Type={hit} | Score={high_calc} | Line={line_count}")
                else:
                    low_calc =  (lower.index(hit)) + 1
                    low_score += low_calc
                    print(f"Type={hit} | Score={low_calc} | Line={line_count}")
            else:
                print(f"----> Type={hit} | Line={clean} | Line={line_count}")
            # reset for next group
            group = []
            group_counter = 0

        group_counter += 1
        line_count+=1

answer = high_score + low_score
print (f"Score={answer} | High={high_score} | Low={low_score}")


