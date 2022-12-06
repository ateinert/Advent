

inputfile = "day4.txt"
filestream = open(inputfile)

overlap_count = 0
overlap = False
count = 1
for line in filestream:

    overlap = False
    left, right = line.strip().split(',')
    left_low, left_high = left.split('-')
    right_low, right_high = right.split('-')
    


    left_list = list(range(int(left_low),int(left_high)+1))
    right_list = list(range(int(right_low),int(right_high)+1))


    intersect = list(set(left_list) & set(right_list))


    if intersect == left_list or intersect == right_list:
        print("Set: ", count)
        #print("\tIntersect: \n\t", intersect)
        overlap = True
        overlap_count += 1


        print("\tLeft: ", left)
        #print("\t", left_list)
        print("\tRight: ", right)
        #print("\t", right_list)
        print("\tOverlap: ", overlap)
        print()

    count += 1
    #if count % 100 == 1:
    #    input("Press any key to continue... ")

print ("Overlap count: ", overlap_count)