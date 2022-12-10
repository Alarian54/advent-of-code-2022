# Parsing
file = open('../data/data10.txt', 'r')
data = file.read()
file.close()
lines = data.split("\n")

# Part 1
cycle = 0
x = 1
xVals = []
for line in lines:
    if line=="noop":
        cycle += 1
        xVals += [x]
    else:
        num = int(line.split(" ")[1])
        cycle += 2
        xVals += [x, x]
        x += num

total = 0
for cycle in [20, 60, 100, 140, 180, 220]:
    total += (xVals[cycle-1]*cycle)
print(total)

# Part 2
screen = [" "]*240
cycle = 0
x = 1
spritePos = [0, 1, 2]

for line in lines:
    if line=="noop":
        if (cycle%40) in spritePos: screen[cycle] = "#"
        cycle += 1
    else:
        if (cycle%40) in spritePos: screen[cycle] = "#"
        cycle += 1
        if (cycle%40) in spritePos: screen[cycle] = "#"
        cycle += 1
        x += int(line.split(" ")[1])
        spritePos = [x-1, x, x+1]

for i in range(6):
    for j in range((i*40), ((i+1)*40)):
        print(screen[j], end="")
    print()