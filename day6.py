inputfile = "day6.txt"
filestream = open(inputfile)
input_string = filestream.read()

packet_length = 14

count = 0
packet_start = []
for element in input_string:
    if len(packet_start) == packet_length:
        if len(set(packet_start)) == packet_length:
            print(count)
            exit()
        packet_start.pop(0)
    packet_start.append(element)
    count += 1
