#Setup
import re

file = open('../data/data16.txt', 'r')
data = file.read()
file.close()
lines = data.split("\n")

names = []
for i in range(len(lines)):
    names += re.search(r"Valve (..) has", lines[i]).groups()

vs = [[] for _ in names]
for i in range(len(lines)):
    regexp = re.search(r"=(.*);.*valves? (.*)", lines[i])
    flow = int(regexp.groups()[0])
    tunnels = [names.index(tunnel) for tunnel in regexp.groups()[1].split(", ")]        
    vs[i] = [i, flow, tunnels, False]

rvs, rvis = [], []
for v in range(len(vs)):
    if vs[v][1] > 0:
        rvs += [vs[v]]
        rvis += [v]

def bfs(vs, start):
    queue = []
    vs[start][3] = True
    queue += [(start, 1)]
    dists = [0 for _ in vs]
    while queue:
        v, dist = queue[0]
        del queue[0]
        dists[v] = dist
        for tunnel in vs[v][2]:
            if not vs[tunnel][3]:
                vs[tunnel][3] = True
                queue += [(tunnel, dist+1)]
    for v in vs:
        v[3] = False
    return dists

distsGrid = [[0 for _ in vs] for _ in vs]
start = 0
for i in range(len(vs)):
    distsGrid[i] = bfs(vs, i)

# Part 1
paths = []
maxFlow = 0
queue = [([0], 30, 0)]
while queue:
    path, mins, flow = queue[0]
    v = path[-1]
    remaining = [v for v in rvis if v not in path]
    newPath = False
    for vn in remaining:
        dist = distsGrid[v][vn]
        if dist < mins:
            minsLeft = mins - dist
            queue += [(path + [vn], minsLeft, (flow + (minsLeft * vs[vn][1])))]
            newPath = True
    if not newPath:
        paths += [(flow, path)]
        if flow > maxFlow:
            maxFlow, bestPath = flow, path
    del queue[0]
print(maxFlow)
print(bestPath, "\n")

# Part 2
paths = []
queue = [([0], 26, 0)]
while queue:
    path, mins, flow = queue[0]
    v = path[-1]
    remaining = [v for v in rvis if v not in path]
    for vn in remaining:
        dist = distsGrid[v][vn]
        if dist < mins:
            newPath = path + [vn]
            minsLeft = mins - dist
            newFlow = flow + (minsLeft * vs[vn][1])
            queue += [(newPath, minsLeft, newFlow)]
            paths += [(newFlow, newPath)]
    del queue[0]

percent = (len(paths)**2)//100
maxFlow = 0
i, j = 1, 1
for path1 in paths:
    for path2 in paths:
        if i%percent == 0:
            print(f"{j}%")
            j += 1
        i += 1
        overlap = False
        for v in path2[1][1:]:
            if v in path1[1]: overlap = True
        if not overlap:
            flow = path1[0] + path2[0]
            if flow > maxFlow:
                maxFlow, bestPath1, bestPath2 = flow, path1, path2
print(maxFlow)
print(bestPath1)
print(bestPath2, "\n")