inputfile = "day8.txt"
filestream = open(inputfile)

forest = []
for line in filestream:
    forest.append(list(line.strip()))

# explore the forest
max_i = len(forest)
max_j = len(forest[0])

visible_count = 0
best_score = 0
for i in range(0, max_i):
    for j in range(0, max_j):
        saved_i = i
        saved_j = j
        visible_up = True
        visible_down = True
        visible_left = True
        visible_right = True
        up_score = 0
        down_score = 0
        left_score = 0
        right_score = 0
        focused_tree = forest[i][j]
        #print(focused_tree)
        #left
        while i > 0:
            i -= 1
            left_score = abs(i - saved_i)
            if forest[i][j] >= focused_tree and visible_left:
                visible_left = False
                break
        i = saved_i
        #right
        while i < max_i - 1:
            i += 1
            right_score = abs(i - saved_i)
            if forest[i][j] >= focused_tree and visible_right:
                visible_right = False
                break
        i = saved_i
        #up
        while j > 0:
            j -= 1
            up_score = abs(j - saved_j)
            if forest[i][j] >= focused_tree and visible_up:
                visible_up = False
                break
        j = saved_j
        #down
        while j < max_j - 1:
            j += 1
            down_score = abs(j - saved_j)
            if forest[i][j] >= focused_tree and visible_down:
                visible_down = False
                break
        j = saved_j
        scenic_score = up_score * down_score * left_score * right_score
        
        #print("Position: ", i, j,"| Height: ", focused_tree, "| score: ", scenic_score)
        #print ("Up",up_score,"Down",down_score,"Left",left_score,"Right",right_score," = ",scenic_score)

        if scenic_score > best_score:
            best_score = scenic_score
        #print(focused_tree, saved_i, saved_j, visible_left, visible_right, visible_down, visible_up)
        if visible_left or visible_right or visible_down or visible_up:
            visible_count += 1

print("Part 1: ",visible_count)
print("Part 2: ",best_score)
