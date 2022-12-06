

inputfile = "day3.txt"
filestream = open(inputfile)

lines = filestream.readlines()

score = 0
total = 0
overlaps = []
for i in range(0,len(lines), 3):
    line1 = lines[i].strip()
    line2 = lines[i+1].strip()
    line3 = lines[i+2].strip()

    common_characters = ''.join(set(line1).intersection(line2).intersection(line3))
    print("Overlap: " + common_characters)
    #print()
    overlaps.append(common_characters)

total = 0
for i in overlaps:
    value = ord(i)
    if value < 97:
        value = value - 65 + 27
    else :
        value = value - 96
    print(i + ": " + str(value))
    total += value

print(total)