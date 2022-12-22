# Setup
file = open('../data/data00.txt', 'r')
file = open('../data/data22.txt', 'r')
data = file.read().split("\n")
file.close()

def printM(map):
    for line in map:
        print(line)

path = data[-1] + "E"
map = data[:-2]

height = len(map)
width = max([len(row) for row in map])
map = [row + " "*(width-len(row)) for row in map]

print("..A.\nBCD.\n..EF\n")
print(".BA\n.C.\nED.\nF..\n")

# print(f"Path to follow: {path}\n")
# print("Map to navigate:")
# printM(map)
# print()

# Part 1
r, c, d = 0, 0, 0
while map[r][c] != ".": c += 1
print(f"Starting pos = row {r}, col {c}. Facing {d}")

i = 0
while i < len(path)-1:
    if path[i].isnumeric():
        num = path[i]
        i += 1
        while path[i].isnumeric():
            num += path[i]
            i += 1
        inst = int(num)
    else:
        inst = path[i]
        i += 1

    if inst == "L": d = (d-1) % 4
    elif inst == "R": d = (d+1) % 4
    else:
        j = 0
        while j < inst:
            if d == 0: nr, nc = r, (c+1) % width
            elif d == 1: nr, nc = (r+1) % height, c
            elif d == 2: nr, nc = r, (c-1) % width
            elif d == 3: nr, nc = (r-1) % height, c
            next = map[nr][nc]
            while next == " ":
                if d == 0: nr, nc = r, (nc+1) % width
                elif d == 1: nr, nc = (nr+1) % height, c
                elif d == 2: nr, nc = r, (nc-1) % width
                elif d == 3: nr, nc = (nr-1) % height, c
                next = map[nr][nc]
            if next == "#":
                j = inst
            elif next == ".":
                r, c = nr, nc
                j += 1

print(f"Final pos = row {r}, col {c}. Facing {d}")
final = (1000 * (r+1)) + (4 * (c+1)) + d
print(f"Final password: {final}\n")

# Part 2
# sideWidth = 50  
# def getSide(r, c):
#     sides = {(0, 2): "A", (0, 1): "B", (1, 1): "C", (2, 1): "D", (2, 0): "E", (3, 0): "F"}  
#     return sides[(r//sideWidth, c//sideWidth)]

r, c, d = 0, 0, 0
while map[r][c] != ".": c += 1
print(f"Starting pos = row {r}, col {c}. Facing {d}")
# print(f"Side: {getSide(r, c)}")


i = 0
# while i < 4:
while i < len(path)-1:
    if path[i].isnumeric():
        num = path[i]
        i += 1
        while path[i].isnumeric():
            num += path[i]
            i += 1
        inst = int(num)
    else:
        inst = path[i]
        i += 1
    # print(f"Instruction: {inst}")

    if inst == "L": d = (d-1) % 4
    elif inst == "R": d = (d+1) % 4
    else:
        j = 0
        while j < inst:
            nr, nc, nd = r, c, d

            if d == 0:
                if c == 49:
                    if r <= 149: nc += 1
                    elif r <= 199: nr, nc, nd = 149, r-100, 3
                elif c == 99:
                    if r <= 49: nc += 1
                    elif r <= 99: nr, nc, nd = 49, r+50, 3
                    elif r <= 149: nr, nc, nd = 149-r, 149, 2
                elif c == 149:
                    if r <= 49: nr, nc, nd = 149-r, 99, 2
                else: nc += 1

            elif d == 1:
                if r == 49:
                    if c <= 99: nr += 1
                    elif c <= 149: nr, nc, nd = c-50, 99, 2
                elif r == 149:
                    if c <= 49: nr += 1
                    elif c <= 99: nr, nc, nd = c+100, 49, 2
                elif r == 199:
                    if c <= 49: nr, nc = 0, c+100
                else: nr += 1

            elif d == 2:
                if c == 0:
                    if r <= 149: nr, nc, nd = 149-r, 50, 0
                    elif r <= 199: nr, nc, nd = 0, r-100, 1
                elif c == 50:
                    if r <= 49: nr, nc, nd = 149-r, 0, 0
                    elif r <= 99: nr, nc, nd = 100, r-50, 1
                    elif r <= 149: nc -= 1
                else: nc -= 1

            elif d == 3:
                if r == 0:
                    if c <= 99: nr, nc, nd = c+100, 0, 0
                    elif c <= 149: nr, nc = 199, c-100
                elif r == 100:
                    if c <= 49: nr, nc, nd = c+50, 50, 0
                    elif c <= 99: nr -= 1
                else: nr -= 1

            next = map[nr][nc]
            if next == "#":
                # print("#")
                j = inst
            elif next == ".":
                # print(".")
                r, c, d = nr, nc, nd
                j += 1
            # print(r, c)

    # print(f"Pos = row {r}, col {c}. Facing {d}")
    # print(f"Side: {getSide(r, c)}")
    # print()

print(f"Final pos = row {r}, col {c}. Facing {d}")
final = (1000 * (r+1)) + (4 * (c+1)) + d
print(f"Final password: {final}")