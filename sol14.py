# Setup
file = open('../data/data14.txt', 'r')
data = file.read()
file.close()
lines = data.split("\n")

minX, minY, maxX, maxY = 1000, 0, 0, 0
for line in lines:
    coords = line.split(" -> ")
    for coord in coords:
        x, y = list(map(int, coord.split(",")))
        if x<minX: minX = x
        if x>maxX: maxX = x
        if y>maxY: maxY = y

def fill(cave):
    for line in lines:
        coords = line.split(" -> ")
        for i in range(1, len(coords)):
            curPos = list(map(int, coords[i-1].split(",")))
            newPos = list(map(int, coords[i].split(",")))
            cave[curPos[1]][curPos[0]-minX] = "#"
            cave[newPos[1]][newPos[0]-minX] = "#"
            if curPos[0]==newPos[0]:
                if curPos[1]<newPos[1]:
                    for y in range(curPos[1], newPos[1]):
                        cave[y][newPos[0]-minX] = "#"
                else:
                    for y in range(newPos[1], curPos[1]):
                        cave[y][newPos[0]-minX] = "#"
            else:
                if curPos[0]<newPos[0]:
                    for x in range(curPos[0], newPos[0]):
                        cave[newPos[1]][x-minX] = "#"
                else:
                    for x in range(newPos[0], curPos[0]):
                        cave[newPos[1]][x-minX] = "#"
    return cave

def printCave(cave):
    for row in cave:
        for point in row:
            print(point, end="")
        print()

# Part 1
cave = [["." for _ in range(maxX+1-minX)] for _ in range(maxY+1-minY)]
cave[0][500-minX] = "+"
cave = fill(cave)

sand = 0
full = False
while cave[0][500-minX]=="+" and not full:
    moving = True
    x, y = 500, 0
    while moving and not full:
        if y==(maxY+1): full = True
        elif cave[y+1][x-minX]==".":
            y += 1
        elif x==minX: full = True
        elif cave[y+1][x-minX-1]==".":
            y += 1
            x -= 1
        elif x==maxX: full = True 
        elif cave[y+1][x-minX+1]==".":
            y += 1
            x += 1
        else: moving = False
    if not full:
        cave[y][x-minX] = "o"
        sand += 1    
print(sand)

# Part 2
minX -= maxY
maxX += maxY
cave = [["." for _ in range(maxX+1-minX)] for _ in range(maxY+3-minY)]
cave[0][500-minX] = "+"
cave = fill(cave)
for i in range(len(cave[0])):
    cave[-1][i] = "#"

sand = 0
while cave[0][500-minX]=="+":
    moving = True
    x, y = 500, 0
    while moving:
        if cave[y+1][x-minX]==".":
            y += 1
        elif cave[y+1][x-minX-1]==".":
            y += 1
            x -= 1
        elif cave[y+1][x-minX+1]==".":
            y += 1
            x += 1
        else: moving = False
    cave[y][x-minX] = "o"
    sand += 1
print(sand)