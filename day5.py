stacks = [
    ['D','H','N','Q','T','W','V','B'],
    ['D','W','B'],
    ['T','S','Q','W','J','C'],
    ['F','J','R','N','Z','T','P'],
    ['G','P','V','J','M','S','T'],
    ['B','W','F','T','N'],
    ['B','L','D','Q','F','H','V','N'],
    ['H','P','F','R'],
    ['Z','S','M','B','L','N','P','H']
]
stacks2 = [
    ['D','H','N','Q','T','W','V','B'],
    ['D','W','B'],
    ['T','S','Q','W','J','C'],
    ['F','J','R','N','Z','T','P'],
    ['G','P','V','J','M','S','T'],
    ['B','W','F','T','N'],
    ['B','L','D','Q','F','H','V','N'],
    ['H','P','F','R'],
    ['Z','S','M','B','L','N','P','H']
]

inputfile = "day5.txt"
filestream = open(inputfile)

for line in filestream:
    words = line.strip().split(' ')
    from_stack = int(words[3])-1
    to_stack = int(words[5])-1
    move_count = int(words[1])

    #print(move_count, from_stack, to_stack)
    #print(stacks2[from_stack])
    #print(stacks2[to_stack])
    for i in range(0,move_count):
        stacks[to_stack].append(stacks[from_stack].pop())
    for i in range(-move_count,0):
        #print(i)
        stacks2[to_stack].append(stacks2[from_stack].pop(i))
        #print(stacks2[from_stack])
        #print(stacks2[to_stack])

crates = []
crates2 = []
for stack in stacks:
    crates.append(stack[-1])
for stack in stacks2:
    crates2.append(stack[-1])
print('Part 1: ',''.join(crates))
print('Part 2: ',''.join(crates2))