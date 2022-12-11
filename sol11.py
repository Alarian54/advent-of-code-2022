# Parsing
file = open('../data/data11.txt', 'r')
data = file.read()
file.close()
lines = data.split("\n")
numMonkeys = (len(lines)+1)//7

def getMonkeys():
    monkeys = [[[], "", "", "", "", ""] for _ in range(numMonkeys)]
    i = 0
    while i<len(lines):
        monkeys[i//7][0] = lines[i+1].split(": ")[1].split(", ")
        monkeys[i//7][1], monkeys[i//7][2] = lines[i+2].split("old ")[1].split(" ")
        monkeys[i//7][3] = int(lines[i+3].split(" by ")[1])
        monkeys[i//7][4] = int(lines[i+4].split("ey ")[1])
        monkeys[i//7][5] = int(lines[i+5].split("ey ")[1])
        for j in range(len(monkeys[i//7][0])):
            monkeys[i//7][0][j] = int(monkeys[i//7][0][j])
        i += 7
    return monkeys

# Part 1
monkeys = getMonkeys()
inspections = [0]*numMonkeys
for round in range(20):
    i = 0
    for monkey in monkeys:
        for item in monkey[0]:
            inspections[i] += 1
            if monkey[1]=="*":
                if monkey[2]=="old": item = item**2
                else: item *= int(monkey[2])
            else:
                if monkey[2]=="old": item = item*2
                else: item += int(monkey[2])
            item = item//3
            if (item%(monkey[3]))==0: monkeys[monkey[4]][0] += [item]
            else: monkeys[monkey[5]][0] += [item]
        monkey[0] = []
        i += 1

inspections.sort()
print(inspections[-1]*inspections[-2])

# Part 2
monkeys = getMonkeys()
inspections = [0]*numMonkeys

totalMod = 1
for monkey in monkeys:
    totalMod *= monkey[3]

for round in range(10000):
    i = 0
    for monkey in monkeys:
        for item in monkey[0]:
            inspections[i] += 1
            if monkey[1]=="*":
                if monkey[2]=="old": item = item**2
                else: item *= int(monkey[2])
            else:
                if monkey[2]=="old": item = item*2
                else: item += int(monkey[2])
            item = item%totalMod
            if (item%(monkey[3]))==0: monkeys[monkey[4]][0] += [item]
            else: monkeys[monkey[5]][0] += [item]
        monkey[0] = []
        i += 1

inspections.sort()
print(inspections[-1]*inspections[-2])