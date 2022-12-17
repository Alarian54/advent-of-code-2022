#Setup
file = open('../data/data17.txt', 'r')
jets = file.read()
file.close()

maxHeight = 100
cave = [["." for _ in range(7)] for _ in range(maxHeight)]
cave[0] = "#######"

lenJets = len(jets)
# numRocks = 2022
numRocks = 1000000000000

i, j = 0, 0
highest, highestExtra = 0, 0
positions = {}
loopStart, loopDuration = 0, 0

# Parts 1 and 2
while i < numRocks:
    overlap = highest+5-maxHeight
    if highest > (maxHeight-5):
        overlap = 20
        for k in range(maxHeight-overlap):
            cave[k] = cave[k+overlap]
        for k in range(maxHeight-overlap, maxHeight):
            cave[k] = ["." for _ in range(7)]
        highestExtra += overlap
        highest -= overlap

    def belowRock(rock, y, x):
        if rock == 0: return [cave[y-1][x], cave[y-1][x+1], cave[y-1][x+2], cave[y-1][x+3]]
        if rock == 1: return [cave[y][x], cave[y-1][x+1], cave[y][x+2]]
        if rock == 2: return [cave[y-1][x], cave[y-1][x+1], cave[y-1][x+2]]
        if rock == 3: return [cave[y-1][x]]
        if rock == 4: return [cave[y-1][x], cave[y-1][x+1]]

    def rightRock(rock, y, x):
        if rock == 0: return [cave[y][x+4]]
        if rock == 1: return [cave[y][x+2], cave[y+1][x+3], cave[y+2][x+2]]
        if rock == 2: return [cave[y][x+3], cave[y+1][x+3], cave[y+2][x+3]]
        if rock == 3: return [cave[y][x+1], cave[y+1][x+1], cave[y+2][x+1], cave[y+3][x+1]]
        if rock == 4: return [cave[y][x+2], cave[y+1][x+2]]

    def leftRock(rock, y, x):
        if rock == 0: return [cave[y][x-1]]
        if rock == 1: return [cave[y][x], cave[y+1][x-1], cave[y+2][x]]
        if rock == 2: return [cave[y][x-1], cave[y+1][x+1], cave[y+1][x+1]]
        if rock == 3: return [cave[y][x-1], cave[y+1][x-1], cave[y+2][x-1], cave[y+3][x-1]]
        if rock == 4: return [cave[y][x-1], cave[y+1][x-1]]

    def rockPoints(rock, y, x):
        if rock == 0: return [(y, x), (y, x+1), (y, x+2), (y, x+3)]
        if rock == 1: return [(y, x+1), (y+1, x), (y+1, x+1), (y+1, x+2), (y+2, x+1)]
        if rock == 2: return [(y, x), (y, x+1), (y, x+2), (y+1, x+2), (y+2, x+2)]
        if rock == 3: return [(y, x), (y+1, x), (y+2, x), (y+3, x)]
        if rock == 4: return [(y, x), (y+1, x), (y, x+1), (y+1, x+1)]
    
    y, x = highest + 1, 2
    rock = i % 5
    maxR = 6 - [4, 3, 3, 1, 2][rock]
    for _ in (1, 2, 3):
        if jets[j] == ">" and x <= maxR:
            x += 1
        elif jets[j] == "<" and x >= 1:
            x -= 1
        j = (j + 1) % lenJets

    while "#" not in belowRock(rock, y, x):
        y -= 1
        if jets[j] == ">" and x <= maxR and "#" not in rightRock(rock, y, x):
            x += 1
        if jets[j] == "<" and x >= 1 and "#" not in leftRock(rock, y, x):
            x -= 1
        j = (j+1) % lenJets
    for (y, x) in rockPoints(rock, y, x):
        cave[y][x] = "#"
    highest = max(highest, y+[0, 2, 2, 3, 1][rock])

    if loopStart == 0:
        key = str(rock) + str(j)
        for row in cave:
            for item in row:
                key += item
        if key in positions:
            loopStart = positions[key][0]
            loopDuration = i - loopStart
            loopHeight = (highest + highestExtra) - positions[key][1]
            remainingLoops = (numRocks - i) // loopDuration
            i += (remainingLoops*loopDuration)
            highestExtra += (remainingLoops*loopHeight)
        else:
            positions[key] = (i, highest + highestExtra)
    i += 1

print(highest + highestExtra)