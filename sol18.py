#Setup
import numpy as np
import re

file = open('../data/data18.txt', 'r')
data = file.read().split("\n")
file.close()

maxX, maxY, maxZ = 0, 0, 0
for cube in data:
    regexp = re.search(r"(.*),(.*),(.*)", cube)
    x, y, z = list(map(int, regexp.groups()))
    if x > maxX: maxX = x
    if y > maxY: maxY = y
    if z > maxZ: maxZ = z
space = np.zeros((maxX+2, maxY+2, maxZ+2))

cubes = []
for cube in data:
    regexp = re.search(r"(.*),(.*),(.*)", cube)
    x, y, z = list(map(int, regexp.groups()))
    space[x, y, z] = -1
    cubes += [(x, y, z)]

# Part 1
directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
surfaceArea = 6 * len(cubes)
for cube in cubes:
    (x, y, z) = cube
    for (x_, y_, z_) in directions:
        surfaceArea += space[x+x_, y+y_, z+z_]
print(int(surfaceArea))

# Part 2
queue = [(0, 0, 0)]
space[0, 0, 0] = 1
while queue:
    x, y, z = queue[0]
    for (x_, y_, z_) in directions:
        nx, ny, nz = x+x_, y+y_, z+z_
        if nx in range(maxX+2):
            if ny in range(maxY+2):
                if nz in range(maxZ+2):
                    if space[nx, ny, nz] == 0:
                        space[nx, ny, nz] = 1
                        queue += [(nx, ny, nz)]
    del queue[0]

for x in range(1, maxX+1):
    for y in range(1, maxY+1):
        for z in range(1, maxZ+1):
            if space[x, y, z]==0:
                innerSpaces = 0
                for (x_, y_, z_) in directions:
                    innerSpaces -= space[x+x_, y+y_, z+z_]
                surfaceArea -= innerSpaces
print(int(surfaceArea))
