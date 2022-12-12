inputfile = "day10.txt"
filestream = open(inputfile)

x = 1
cycle_count = 0
values = []
part2 = ""
for line in filestream:
    commands = line.strip().split(" ")
    command = commands[0]
    if len(commands) == 2:
        x_input = int(commands[1])
    if command == "noop":
        cycle_change = 1
    else:
        cycle_change = 2
    i = 0
    while i < cycle_change:
        if (cycle_count - 20) % 40 == 0:
            values.append([cycle_count,x])
        if cycle_count % 40 == 0 and cycle_count != 0:
            part2 += "\n"
        if cycle_count % 40 in [x,x-1,x+1]:
            part2 += "#"
        else:
            part2 += "."
        if command != "noop" and i == cycle_change - 1:
            x += x_input
        cycle_count += 1
        i += 1
    
signal_strenght_sum = 0
for i in range(6):
    signal_strenght = values[i][0] * values[i][1]
    signal_strenght_sum += signal_strenght
print("Part 1: ", signal_strenght_sum)
print("Part 2:")
print(part2)