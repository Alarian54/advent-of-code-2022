import numpy as np

# Parsing
file = open('../data/data8.txt', 'r')
data = file.read()
file.close()
lines = data.split("\n")
trees = np.array([list(map(int, line)) for line in lines])

rows = len(trees)
cols = len(trees[0])

# Part 1
visible = np.zeros((rows, cols))

def traverse(range1, range2):
    for i in range1:
        maxHeight = -1
        for j in range2:
            tree = trees[i, j]
            if tree>maxHeight:
                visible[i, j] = 1
                maxHeight = tree

traverse(range(rows), range(cols))
traverse(range(rows), range(cols-1, -1, -1))
trees, visible = np.transpose(trees), np.transpose(visible)
traverse(range(rows), range(cols))
traverse(range(rows), range(cols-1, -1, -1))

print(int(np.sum(visible)))

# Part 2
maxScore = 0
for i in range(1, rows-1):
    for j in range(1, cols-1):
        tree = trees[i, j]
        topDist, bottomDist, leftDist, rightDist = 0, 0, 0, 0
        iLookUp, iLookDown = i-1, i+1
        jLookLeft, jLookRight = j-1, j+1

        while iLookUp>=0:
            topDist += 1
            if trees[iLookUp, j]>=tree: iLookUp = -1
            else: iLookUp -= 1

        while iLookDown<rows:
            bottomDist += 1
            if trees[iLookDown, j]>=tree: iLookDown = rows
            else: iLookDown += 1

        while jLookLeft>=0:
            leftDist += 1
            if trees[i, jLookLeft]>=tree: jLookLeft = -1
            else: jLookLeft -= 1

        while jLookRight<cols:
            rightDist += 1
            if trees[i, jLookRight]>=tree: jLookRight = cols
            else: jLookRight += 1

        viewingScore = topDist*bottomDist*leftDist*rightDist
        if viewingScore > maxScore:
            maxScore = viewingScore

print(maxScore)
