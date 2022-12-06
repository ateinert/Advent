

inputfile = "day2.txt"
filestream = open(inputfile)

score = 0
total = 0
for line in filestream:
    score = 0
    left, right = line.lower().strip().split(' ')
    
    if left == 'a':
        if right == 'x':
            score += 0
            score += 3
        elif right == 'y':
            score += 3
            score += 1
        else:
            score += 6
            score += 2
    elif left == 'b':
        if right == 'x':
            score += 0
            score += 1
        elif right == 'y':
            score += 3
            score += 2
        else:
            score += 6
            score += 3
    else:
        if right == 'x':
            score += 0
            score += 2
        elif right == 'y':
            score += 3
            score += 3
        else:
            score += 6
            score += 1

    print(score)
    total += score


print ("Score")
print (total)
