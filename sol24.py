# Setup
file = open('../data/data24.txt', 'r')
data = file.read().split("\n")
file.close()
rows, cols = len(data), len(data[0])
print(f"Number of possible positions: {((rows-2)*(cols-2))+2}")

blizNorth, blizSouth, blizWest, blizEast = [], [], [], []
for (i, row) in enumerate(data):
    for (j, char) in enumerate(row):
        if data[i][j] == "^": blizNorth.append((i, j))
        elif data[i][j] == "v": blizSouth.append((i, j))
        elif data[i][j] == "<": blizWest.append((i, j))
        elif data[i][j] == ">": blizEast.append((i, j))
blizCutoffs = (len(blizNorth), len(blizNorth)+len(blizSouth), len(blizNorth)+len(blizSouth)+len(blizWest))
blizzards = blizNorth + blizSouth + blizWest + blizEast

moves = ((-1, 0), (1, 0), (0, -1), (0, 1), (0, 0))

# Taking a trip
def minRoute(start, end, blizzards):
    posits = {start}
    reached = False
    # reached = True
    time = 0
    while not reached:
        time += 1

        i = 0
        while i < blizCutoffs[0]:
            r, c = blizzards[i]
            if r == 1: blizzards[i] = (rows-2, c)
            else: blizzards[i] = (r-1, c)
            i += 1
        while i < blizCutoffs[1]:
            r, c = blizzards[i]
            if r == rows-2: blizzards[i] = (1, c)
            else: blizzards[i] = (r+1, c)
            i += 1
        while i < blizCutoffs[2]:
            r, c = blizzards[i]
            if c == 1: blizzards[i] = (r, cols-2)
            else: blizzards[i] = (r, c-1)
            i += 1
        while i < len(blizzards):
            r, c = blizzards[i]
            if c == cols-2: blizzards[i] = (r, 1)
            else: blizzards[i] = (r, c+1)
            i += 1
        
        newPosits = set()
        for posit in posits:
            for move in moves:
                newMove = (posit[0]+move[0], posit[1]+move[1])
                if newMove == end:
                    reached = True
                elif newMove == start:
                    newPosits.add(newMove)
                elif newMove[0] > 0:
                    if newMove[0] < rows-1:
                        if newMove[1] > 0:
                            if newMove[1] < cols-1:
                                if newMove not in blizzards:
                                    newPosits.add(newMove)
        posits = newPosits
        print(f"Time step: {time},", end="  ")
        print(f"Positions: {len(posits)}")
    return time, blizzards

# Taking the trips
print("Trip 1:")
trip1, blizzards = (minRoute((0, 1), (rows-1, cols-2), blizzards))
print("\nTrip 2:")
trip2, blizzards = (minRoute((rows-1, cols-2), (0, 1), blizzards))
print("\nTrip 3:")
trip3, blizzards = (minRoute((0, 1), (rows-1, cols-2), blizzards))
print(f"\nTime for 1 trip: {trip1} minutes")
print(f"Time for 3 trips: {trip1 + trip2 + trip3} minutes")
