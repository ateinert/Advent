import ast
import functools

inputfile = "day13.txt"

def correctOrder(left, right):
    for i in range(len(left)):
        try:
            order = None
            if type(left[i]) == type(right[i]) and type(left[i]) is int:
                if left[i] < right[i]:
                    return True
                elif left[i] > right[i]:
                    return False
                elif i == len(left) - 1 and i < len(right) - 1:
                    return True
            elif type(left[i]) == type(right[i]):
                order = correctOrder(left[i], right[i])
            else:
                if type(left[i]) is int:
                    left_copy = [left[i]]
                    order = correctOrder(left_copy, right[i])
                else:
                    right_copy = [right[i]]
                    order = correctOrder(left[i], right_copy)
            if order is not None:
                return order
        except Exception:
            return False
    if len(left) < len(right):
        return True


filestream = open(inputfile).readlines()
correctIndexesSum = 0
packets = [[[2]],[[6]]]

index = 1
for i in range(0,len(filestream), 3):
    left = ast.literal_eval(filestream[i].strip())
    right = ast.literal_eval(filestream[i+1].strip())

    order = correctOrder(left, right)
    if order is None:
        print("Error")
        exit()

    if order:
        correctIndexesSum += index
    index += 1

    packets.append(left)
    packets.append(right)

index_1 = 0
index_2 = 0
temp_index = 1
sorted_packets = sorted(packets, key=functools.cmp_to_key(lambda a, b : -1 if correctOrder(a, b) else 1 if correctOrder(b, a) else 0))
for i in sorted_packets:
    if i == [[2]]:
        print (i)
        index_1 = temp_index
    if i == [[6]]:
        print (i)
        index_2 = temp_index
    temp_index += 1
        

print("Part 1:", correctIndexesSum)
print("Part 2:", index_1*index_2)