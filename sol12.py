import numpy as np

# Parsing
file = open('../data/data12.txt', 'r')
data = file.read()
file.close()
lines = data.split("\n")
rows, cols = len(lines), len(lines[0])

heights = "abcdefghijklmnopqrstuvwxyz"
def getGrid():
    grid = [[{} for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if lines[i][j]=="S":
                lowPos = (i, j)
                grid[i][j]["height"] = 0
            elif lines[i][j]=="E":
                highPos = (i, j)
                grid[i][j]["height"] = 25
            else:
                grid[i][j]["height"] = int(heights.index(lines[i][j]))
            grid[i][j]["length"] = np.inf
            grid[i][j]["unvisited"] = True
    return grid, lowPos, highPos

# Part 1
grid, startPos, endPos = getGrid()
curX, curY = startPos
grid[curX][curY]["length"] = 0

visited = 0
while visited<(rows*cols):
    for node in [(curX+1, curY), (curX-1, curY), (curX, curY+1), (curX, curY-1)]:
        newX, newY = node
        if newX>=0 and newX<rows and newY>=0 and newY<cols:
            if grid[newX][newY]["unvisited"]:
                if (grid[newX][newY]["height"] - grid[curX][curY]["height"])<=1:
                    grid[newX][newY]["length"] = min(grid[curX][curY]["length"]+1, grid[newX][newY]["length"])
    grid[curX][curY]["unvisited"] = False
    visited += 1
    if endPos==(curX, curY):
        print(grid[curX][curY]["length"])
        visited = rows*cols
    minDist = np.inf
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]["unvisited"]:
                if grid[i][j]["length"]<minDist:
                    curX, curY = i, j
                    minDist = grid[i][j]["length"]

# Part 2
grid, _, startPos = getGrid()
curX, curY = startPos
grid[curX][curY]["length"] = 0

visited = 0
while visited<(rows*cols):
    for node in [(curX+1, curY), (curX-1, curY), (curX, curY+1), (curX, curY-1)]:
        newX, newY = node
        if newX>=0 and newX<rows and newY>=0 and newY<cols:
            if grid[newX][newY]["unvisited"]:
                if (grid[curX][curY]["height"] - grid[newX][newY]["height"])<=1:
                    grid[newX][newY]["length"] = min(grid[curX][curY]["length"]+1, grid[newX][newY]["length"])
    grid[curX][curY]["unvisited"] = False
    visited += 1
    if grid[curX][curY]["height"]==0:
        print(grid[curX][curY]["length"])
        visited = rows*cols
    minDist = np.inf
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]["unvisited"]:
                if grid[i][j]["length"]<minDist:
                    curX, curY = i, j
                    minDist = grid[i][j]["length"]