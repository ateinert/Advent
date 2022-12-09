class Rope:
    def __init__(self, knots_count):
        self.knots = [[0,0] for i in range(knots_count)]
        self.knots_count = knots_count
    def getHead(self):
        return self.knots[0]
    def getTail(self):
        return self.knots[-1]
    def move(self, direction):
        movement = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}
        x,y = movement[direction]
        self.knots[0][0] += x
        self.knots[0][1] += y
        for i in range(1, self.knots_count):
            px,py = self.knots[i-1]
            cx,cy = self.knots[i]
            if max(abs(px - cx), abs(py - cy)) > 1:
                if px != cx:
                    cx += 1 if px > cx else -1
                if py != cy:
                    cy += 1 if py > cy else -1
            self.knots[i][0] = cx
            self.knots[i][1] = cy

inputfile = "day9.txt"
filestream = open(inputfile)
rope = Rope(2)
rope2 = Rope(10)
tail_positions = set()
tail_positions2 = set()

for line in filestream:
    direction, distance = line.strip().split(" ")
    distance = int(distance)
    for i in range(distance):
        rope.move(direction)
        rope2.move(direction)
        tail_positions.add(tuple(rope.getTail()))
        tail_positions2.add(tuple(rope2.getTail()))

print("Part 1: ", len(set(tail_positions)))
print("Part 2: ", len(set(tail_positions2)))