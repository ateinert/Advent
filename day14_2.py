minX = 999999999
maxX = 0
maxY = 0

def generateMatrix(spawn):
# generate matrix
    matrix = [["." for _ in range(maxX - minX + 1)] for _ in range(maxY)]
    matrix[spawn[1]][spawn[0] - minX] = "+"
    return matrix

def printMatrix(matrix):
# print the matrix
    row_count = 0
    for row in matrix:
        print (f'{row_count:>3}', end = " ")
        row_count += 1
        for x in row:
            print(x, end='')
        print()

def placeStructures(matrix, structures):
    for struct in structures:
        #print(struct)
        i = 1
        while i < len(struct):
            x,y = struct[i-1]
            x -= minX
            end_x,end_y = struct[i]
            end_x -= minX
            while x != end_x:
                matrix[y][x] = "#"
                x += 1 if x < end_x else -1
            while y != end_y:
                matrix[y][x] = "#"
                y += 1 if y < end_y else -1
            i += 1
        matrix[end_y][end_x] = "#"
    return matrix
        
def dropSand(matrix, spawn):  
    sand = list(spawn)
    sand[0] -= minX
    try:
        # keep going
        while True:
            if matrix[sand[1] + 1][sand[0]] == ".":
                sand[1] += 1
            # down left
            elif matrix[sand[1] + 1][sand[0] - 1] == ".":
                sand[0] -= 1
                sand[1] += 1
            # down right
            elif matrix[sand[1] + 1][sand[0] + 1] == ".":
                sand[0] += 1
                sand[1] += 1
            # filled the hole
            elif sand == [spawn[0] - minX, spawn[1]]:
                return False
            # nowhere to go, but safe
            else:
                matrix[sand[1]][sand[0]] = 'o'
                return True
    except Exception:
        print(sand)
        print("FAIL")
        return False

inputfile = "day14.txt"
filestream = open(inputfile).readlines()
spawn = (500,0)

# ingest the struc cordinates
structures = []
for line in filestream:
    structure = []
    cordinate_sets = line.strip().split(" -> ")
    for cordinates in cordinate_sets:
        x = int(cordinates.split(",")[0])
        y = int(cordinates.split(",")[1])
        if x < minX:
            minX = x
        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y
        structure.append((x,y))
    structures.append(structure)
minX = 0
maxX += 500
maxY += 3
structure = ((minX,maxY-1),(maxX, maxY-1))
structures.append(structure)

matrix = generateMatrix(spawn)
matrix = placeStructures(matrix, structures)

count = 1
while dropSand(matrix, spawn):
    count += 1

#printMatrix(matrix)

print("Part 2:", count)