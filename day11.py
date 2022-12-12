import operator
import functools

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
}

class Monkey():
    def __init__(self, items, operation_str, test_str, action_str_true,action_str_false):
        self.items = items
        self.inspect_count = 0
        self.divisor = int(test_str.split(" ")[2])
        def operation(worry):
            value1, op, value2 = operation_str.split(" ")
            if value1 == "old":
                value1 = worry
            if value2 == "old":
                value2 = worry
            
            return ops[op](int(value1),int(value2))
        self.operation = operation

        def test(test):
            # "divisible by 2"
            value = int(test_str.split(" ")[2])
            return test % value == 0
        self.test = test

        def action(value):
            if value:
                monkey = action_str_true.split(" ")[-1]
            else:
                monkey = action_str_false.split(" ")[-1]
            return monkey
        self.action = action

    def playRound(self, worry_divide, common_divisor):
        item_count = len(self.items)
        actions = []
        for i in range(item_count):
            worry = self.operation(self.items[i])
            self.inspect_count += 1
            worry = worry // worry_divide
            worry = worry % common_divisor
            worry_test = self.test(worry)
            monkey_to = int(self.action(worry_test))
            actions.append((monkey_to,worry))
        self.items = []
        return actions

monkeys = []
monkeys2 = []
inputfile = "day11.txt"
filestream = open(inputfile).readlines()

for i in range(0, len(filestream), 7):
    content = filestream[i + 1: i + 6]

    # Get items
    items = content[0].strip().split(": ")[1].strip().split(", ")
    items = [eval(i) for i in items]
    #print(items)

    # Get operation
    operation = content[1].strip().split(": ")[1].split(" = ")[1]
    #print(operation)

    # Get get
    test = content[2].strip().split(": ")[1]
    #print(test)

    # Get true_action
    true_action = content[3].strip().split(": ")[1]
    #print(true_action)

    # Get false_action
    false_action = content[4].strip().split(": ")[1]
    #print(false_action)
    
    monkey = Monkey(
        items.copy(),
        operation,
        test,
        true_action,
        false_action
    )
    monkey2 = Monkey(
        items.copy(),
        operation,
        test,
        true_action,
        false_action
    )
    monkeys.append(monkey)
    monkeys2.append(monkey2)

common_divisor = functools.reduce(lambda cd, x: cd * x, (m.divisor for m in monkeys))

# Play 20 rounds
for i in range(20):
    for monkey in monkeys:
        actions = monkey.playRound(3,common_divisor)
        for action in actions:
            monkeys[int(action[0])].items.append(action[1])

# Play 10,000 rounds
for i in range(10000):
    for monkey2 in monkeys2:
        actions = monkey2.playRound(1,common_divisor)
        for action in actions:
            monkeys2[int(action[0])].items.append(action[1])


monkeys.sort(key = lambda x: x.inspect_count, reverse=True)
monkeys2.sort(key = lambda x: x.inspect_count, reverse=True)
print("Part 1: ",monkeys[0].inspect_count * monkeys[1].inspect_count)
print("Part 2: ",monkeys2[0].inspect_count * monkeys2[1].inspect_count)