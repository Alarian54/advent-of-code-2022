# Setup
file = open('../data/data00.txt', 'r')
data = file.read().split("\n")
file.close()

# overlap = 50
elves = set()
# map = [["." for _ in range(len(data[0]) + (2*overlap))] for _ in range(len(data) + (2*overlap))]
for (r, row) in enumerate(data):
    for (c, char) in enumerate(row):
        # map[r+overlap][c+overlap] = char
        if char == "#":
            # elves += [(r+overlap, c+overlap)]
            elves.add((r, c))
print(elves)

for round in range(10):
    print(f"Round {round}")

# dirs = [(0, 1, 2, -1, 0), (4, 5, 6, 1, 0), (0, 6, 7, 0, -1), (2, 3, 4, 0, 1)]

# Parts 1 and 2
# round = 0
# elfMoved = True
# while elfMoved:
#     print(f"Round {round+1}")
#     proposed = []
#     # cancelled = []

#     elfMoved = False
#     for (e, (r, c)) in enumerate(elves):
#         surround = (map[r-1][c-1], map[r-1][c], map[r-1][c+1], map[r][c+1], map[r+1][c+1], map[r+1][c], map[r+1][c-1], map[r][c-1])
#         prop = ()
#         if "#" not in surround: prop = (r, c)
#         else:
#             i = 0
#             while i < 4:
#                 dir = dirs[i]
#                 if "#" not in [surround[dir[0]], surround[dir[1]], surround[dir[2]]]: prop, i = (r+dir[3], c+dir[4]), 3
#                 i += 1
#         if prop == (): prop = (r, c)


#         proposed += [prop]
#     for (e, (r, c)) in enumerate(elves):
#         pr, pc = proposed[e]
#         if map[pr][pc] == ".":
#             map[pr][pc] = "#"


#         if prop in proposed: cancelled += [proposed.index(prop), e]
#         elif prop != (r, c): elfMoved = True
#         proposed += [prop]
#     for e in cancelled:
#         proposed[e] = elves[e]
        
#     for e in range(len(elves)):
#         (r, c) = elves[e]
#         map[r][c] = "."
#         (r, c) = proposed[e]
#         map[r][c] = "#"
#         elves[e] = proposed[e]

#     dirs = dirs[1:] + [dirs[0]]
#     round += 1

# minR, maxR, minC, maxC = len(map), 0, len(map[0]), 0
# for (r, c) in elves:
#     if r < minR: minR = r
#     if r > maxR: maxR = r
#     if c < minC: minC = c
#     if c > maxC: maxC = c
# print(f"Number of empty spaces: {((1+maxR-minR)*(1+maxC-minC))-len(elves)}")
# print(f"Rounds taken until no changes: {round}")