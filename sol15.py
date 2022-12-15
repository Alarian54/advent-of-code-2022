# Setup
import re

file = open('../data/data15.txt', 'r')
data = file.read()
file.close()
lines = data.split("\n")

data = []
for line in lines:
    regexp = re.search(r"Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", line)
    sX, sY, bX, bY = list(map(int, regexp.groups()))
    data += [{"sX":sX, "sY":sY, "bX":bX, "bY":bY, "dist":abs(sX-bX) + abs(sY-bY)}]

# Part 1
# targetY = 10
targetY = 2000000
xPositions = set()
for item in data:
    yDist = abs(targetY-item["sY"])
    if yDist <= item["dist"]:
        xDist = abs(item["dist"]-yDist)
        for x in range(xDist+1):
            xPositions.add(item["sX"]-x)
            xPositions.add(item["sX"]+x)
for item in data:
    if item["bY"] == targetY:
        if item["bX"] in xPositions:
            xPositions.remove(item["bX"])
print(len(xPositions))

# Part 2
# maxXY = 20
maxXY = 4000000
for y in range(maxXY+1):
    if y%100000 == 0: print("y =", y)
    xRanges = []
    for item in data:
        yDist = abs(y-item["sY"])
        if yDist <= item["dist"]:
            xDist = abs(item["dist"]-yDist)
            xRanges += [(max(0, item["sX"]-xDist), min(maxXY, item["sX"]+xDist))]

    combining = True
    while combining and len(xRanges)>1:
        i, j, searching = 0, 1, True
        while searching and len(xRanges)>1:
            range1, range2 = xRanges[i], xRanges[j]
            if (range1[1] > range2[0]-1) and (range2[1] > range1[0]-1):
                newRange = (min(range1[0], range2[0]), max(range1[1], range2[1]))
                del xRanges[j]
                del xRanges[i]
                xRanges += [newRange]
                searching = False
            elif j<len(xRanges)-1: j += 1
            elif i<len(xRanges)-2:
                i += 1
                j = i+1
            else: searching, combining = False, False

    if len(xRanges)>1:
        x = min(xRanges[0][1], xRanges[1][1])+1
        print((4000000*x)+y)
        break