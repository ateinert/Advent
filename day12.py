
def ingestFile(inputfile):
    filestream = open(inputfile).readlines()
    matrix = []
    possible_starts = []
    # ingest txt file
    for i in range(len(filestream)):
        matrix.append([])
        line = filestream[i].strip()
        for j in range(len(line)):
            char = line[j]
            if char == 'a':
                possible_starts.append(tuple([i,j]))
            if char == "S":
                char = 1
                start = tuple([i,j])
            elif char == "E":
                char = 26
                end = tuple([i,j])
            else:
                char = ord(char) - 96
            matrix[i].append(char)
    return matrix,start,end,possible_starts

def printMatrix(matrix, start, end, position, path):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            node = tuple([i,j])
            node_value = matrix[i][j]
            if node == start:
                print("S", end = "")
            elif node == end:
                print("E", end = "")
            elif node == position:
                print ("@", end = "")
            elif node in path:
                print('.', end = "")
            else:
                print(chr(node_value + 96), end = "")
        #print("-" * len(i))
        print()

def shortestPath(matrix, start, end):
    path_list = [[start]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {start}
    if start == end:
        return path_list[0]
    
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        # Generate next nodes
        last_node_value = matrix[last_node[0]][last_node[1]]
        next_nodes = []
        # Check down
        if last_node[0] < len(matrix) - 1:
            node = tuple([last_node[0]+1,last_node[1]])
            node_value = matrix[node[0]][node[1]]
            #print("DOWN", node, node_value)
            if node_value > last_node_value and node_value - last_node_value == 1:
                next_nodes.append(node)
            elif node_value <= last_node_value:
                next_nodes.append(node)
        # Check right
        if last_node[1] < len(matrix[0]) - 1:
            node = tuple([last_node[0],last_node[1]+1])
            node_value = matrix[node[0]][node[1]]
            #print("RIGHT", node, node_value)
            if node_value > last_node_value and node_value - last_node_value == 1:
                next_nodes.append(node)
            elif node_value <= last_node_value:
                next_nodes.append(node)
        # Check up
        if last_node[0] > 0:
            node = tuple([last_node[0]-1,last_node[1]])
            node_value = matrix[node[0]][node[1]]
            #print("UP", node, node_value)
            if node_value > last_node_value and node_value - last_node_value == 1:
                next_nodes.append(node)
            elif node_value <= last_node_value:
                next_nodes.append(node)
        # Check left
        if last_node[1] > 0:
            node = tuple([last_node[0],last_node[1]-1])
            node_value = matrix[node[0]][node[1]]
            #print("LEFT", node, node_value)
            if node_value > last_node_value and node_value - last_node_value == 1:
                next_nodes.append(node)
            elif node_value <= last_node_value:
                next_nodes.append(node)
        # Search goal node
        if end in next_nodes:
            current_path.append(end)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    #printMatrix(matrix, start, end, last_node, current_path)
    return []

file = "day12.txt"
matrix,start,end,possible_starts = ingestFile(file)

path = shortestPath(matrix,start,end)
#printMatrix(matrix,start,end,end,path)

shortest_path = path.copy()
for start in possible_starts:
    test_path = shortestPath(matrix,start,end)
    if test_path and  len(test_path) < len(shortest_path) and test_path[-1] == end:
        shortest_path = test_path

#print(path)
print("Part 1:", len(path)-1)
print("Part 2:", len(shortest_path)-1)