

inputfile = "test.txt"
filestream = open(inputfile)

calories = []
count = 0
for line in filestream:
    if line == '\n':
        calories.append(count)
        count = 0
    else:
        item = int(line.strip())
        count = count + item

print ("Highest Calories")
print (max(calories))

calories.sort(reverse=True)
print ("Top 3 Sum")
print(calories[0] + calories[1] + calories[2])