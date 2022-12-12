import copy

# Parsing
file = open('../data/data5.txt', 'r')
data = file.read()
file.close()
lines = data.split("\n")

line = lines[0]
numStacks = (len(line)+1)//4
stacks = [[] for _ in range(numStacks)]

i = 0
while "[" in line:
    for j in range(numStacks):
        crate = line[(j*4)+1]
        if crate!=" ":
            stacks[j] = [crate] + stacks[j]
    i += 1
    line = lines[i]

while "move" not in lines[i]:
    i += 1
startingi = i
startingStacks = copy.deepcopy(stacks)

# Part 1
while i<len(lines):
    numCrates = int(lines[i].split(" from ")[0].split(" ")[1])
    origin = int(lines[i].split(" from ")[1].split(" to ")[0])-1
    dest = int(lines[i].split(" from ")[1].split(" to ")[1])-1
    
    for j in range(numCrates):
        stacks[dest] += [stacks[origin][-1]]
        del stacks[origin][-1]
    i += 1

for stack in stacks:
    print(stack[-1], end="")
print()

# Part 2
i = startingi
stacks = startingStacks

while i<len(lines):
    numCrates = int(lines[i].split(" from ")[0].split(" ")[1])
    origin = int(lines[i].split(" from ")[1].split(" to ")[0])-1
    dest = int(lines[i].split(" from ")[1].split(" to ")[1])-1

    stacks[dest] += stacks[origin][(0-numCrates):]
    del stacks[origin][(0-numCrates):]
    i += 1

for stack in stacks:
    print(stack[-1], end="")
print()