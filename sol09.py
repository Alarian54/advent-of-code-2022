# Parsing
file = open('../data/data9.txt', 'r')
data = file.read()
file.close()
instructions = data.split("\n")

# Part 1
locations = {(0, 0)}
hX, hY = 0, 0
tX, tY = 0, 0

def newPos(hX, hY, tX, tY):
    if abs(hX-tX)==2:
        tX += (hX-tX)//2
        if (hY-tY)>0: tY += 1
        elif (hY-tY)<0: tY -= 1
    if abs(hY-tY)==2:
        tY += (hY-tY)//2
        if (hX-tX)>0: tX += 1
        elif (hX-tX)<0: tX -= 1
    return tX, tY

for instruction in instructions:
    dir, leng = instruction.split(" ")
    for _ in range(int(leng)):
        if dir=="U": hY += 1
        elif dir=="R": hX += 1
        elif dir=="D": hY -= 1
        elif dir=="L": hX -= 1

        tX, tY = newPos(hX, hY, tX, tY)
        locations.add((tX, tY))

print(len(locations))

# Part 2
locations = {(0, 0)}
Xvals = [0]*10
Yvals = [0]*10

for instruction in instructions:
    dir, leng = instruction.split(" ")
    for _ in range(int(leng)):
        if dir=="U": Yvals[0] += 1
        elif dir=="R": Xvals[0] += 1
        elif dir=="D": Yvals[0] -= 1
        elif dir=="L": Xvals[0] -= 1

        for i in range(1, len(Xvals)):
            Xvals[i], Yvals[i] = newPos(Xvals[i-1], Yvals[i-1], Xvals[i], Yvals[i])
        locations.add((Xvals[9], Yvals[9]))

print(len(locations))