# Setup
file = open('../data/data21.txt', 'r')
monkeys = file.read().split("\n")
file.close()

# Part 1
yells = {}
while "root" not in yells:
    for monkey in monkeys:
        split = monkey.split(" ")
        name = split[0][:-1]
        yellKeys = yells.keys()
        if name not in yellKeys:
            if split[1].isnumeric():
                yells[name] = int(split[1])
            else:
                if split[1] in yellKeys:
                    if split[3] in yellKeys:
                        x, y = yells[split[1]], yells[split[3]]
                        if split[2] == "+": yells[name] = x + y
                        elif split[2] == "-": yells[name] = x - y
                        elif split[2] == "*": yells[name] = x * y
                        elif split[2] == "/": yells[name] = x // y
print(yells["root"])

# Part 2
consts = {}
initLen = -1
while initLen != len(consts):
    initLen = len(consts)
    for monkey in monkeys:
        split = monkey.split(" ")
        name = split[0][:-1]
        yellKeys = consts.keys()
        if name not in yellKeys and name != "humn":
            if split[1].isnumeric():
                consts[name] = int(split[1])
            else:
                if split[1] in yellKeys:
                    if split[3] in yellKeys:
                        x, y = consts[split[1]], consts[split[3]]
                        if split[2] == "+": consts[name] = x + y
                        elif split[2] == "-": consts[name] = x - y
                        elif split[2] == "*": consts[name] = x * y
                        elif split[2] == "/": consts[name] = x // y

yells = {}
for monkey in monkeys:
    split = monkey.split(" ")
    yells[monkey[:4]] = monkey[6:]
for monkey in monkeys:
    if monkey[:4] == "root":
        eq1 = monkey.split(" ")[1]
        eq2 = consts[monkey.split(" ")[3]]

initLen = 0
while initLen != len(eq1):
    initLen = len(eq1)
    for i in range(len(eq1)-3):
        quad = eq1[i:i+4]
        if quad in consts.keys():
            eq1 = eq1[:i] + str(consts[quad]) + eq1[i+4:]
            continue
        elif quad in yells.keys() and quad != "humn":
            eq1 = eq1[:i] + "(" + yells[quad] + ")" + eq1[i+4:]
            continue

i = 0
while "((" in eq1 or "))" in eq1:
    split = eq1.split(" ")
    if eq1[1] == "(":
        operation = split[-2]
        num = int(split[-1][:-1])
        eq1 = " ".join(split[:-2])[1:]
        numFirst = False
    elif eq1[-2] == ")":
        operation = split[1]
        num = int(split[0][1:])
        eq1 = " ".join(split[2:])[:-1]
        numFirst = True
    if operation == "+": eq2 -= num
    if operation == "-":
        if numFirst: eq2 = num - eq2
        else: eq2 += num
    if operation == "*": eq2 = eq2 // num
    if operation == "/":
        if numFirst: eq2 = num // eq2
        else: eq2 *= num
    i += 1

split = eq1.split(" ")
if split[0][1:].isnumeric():
    num = int(split[0][1:])
    numFirst = True
else:
    num = int(split[2][:-1])
    numFirst = False
operation = split[1]
if operation == "+": eq2 -= num
if operation == "-":
    if numFirst: eq2 = num - eq2
    else: eq2 += num
if operation == "*": eq2 = eq2 // num
if operation == "/":
    if numFirst: eq2 = num // eq2
    else: eq2 *= num

yells = {"humn":int(eq2)}
print(eq2)