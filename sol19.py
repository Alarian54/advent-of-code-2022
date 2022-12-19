#Setup
from math import ceil
import numpy as np
import re
import time

file = open('../data/data19.txt', 'r')
data = file.read().split("\n")
file.close()

blueprints = []
for blueprint in data:
    regexp = re.search(r"sts (.*) ore.*sts (.*) ore.*sts (.*) ore and (.*) clay.*sts (.*) ore and (.*) obs", blueprint)
    ore, cly, obs1, obs2, geo1, geo2 = list(map(int, regexp.groups()))
    blueprints += [(np.array([ore, 0, 0, 0]), np.array([cly, 0, 0, 0]), np.array([obs1, obs2, 0, 0]), np.array([geo1, 0, geo2, 0]))]
newRobot = (np.array([1, 0, 0, 0]), np.array([0, 1, 0, 0]), np.array([0, 0, 1, 0]), np.array([0, 0, 0, 1]))
triangles = [0]
for i in range(32):
    triangles += [triangles[-1]+i]

# Parts 1 and 2
totalQuality = 0
productQuality = 1
for i in range(min(3, len(blueprints))):
    start = time.time()
    blueprint = blueprints[i]
    print(f"Blueprint {i+1}")
    print("Blueprint costs:", blueprint[0], blueprint[1], blueprint[2], blueprint[3])

    resources = np.array([0, 0, 0, 0])
    robots = np.array([1, 0, 0, 0])
    maxOre = max(blueprint[0][0], blueprint[1][0], blueprint[2][0], blueprint[3][0])
    maxCly = blueprint[2][1]
    maxObs = blueprint[3][2]

    mins = 32
    maxGeodes = 0

    queue = [(resources, robots, mins)]
    while queue:
        resources, robots, mins = queue[0]
        if resources[3] + (mins*robots[3]) + triangles[mins] > maxGeodes:
            builtRobot = False

            if robots[0] < maxOre:
                # Work towards building an ore robot
                timeNeeded = 1
                oreNeeded = blueprint[0][0] - resources[0]
                if oreNeeded > 0:
                    timeNeeded += ceil(oreNeeded/robots[0])
                minsLeft = mins - timeNeeded
                if minsLeft > 0:
                    queue += [(resources+(robots*timeNeeded)-blueprint[0], robots+newRobot[0], minsLeft)]
                    builtRobot = True

            if robots[1] < maxCly:
                # Work towards building a clay robot
                timeNeeded = 1
                oreNeeded = blueprint[1][0] - resources[0]
                if oreNeeded > 0:
                    timeNeeded += ceil(oreNeeded/robots[0])
                minsLeft = mins - timeNeeded
                if minsLeft > 0:
                    queue += [(resources+(robots*timeNeeded)-blueprint[1], robots+newRobot[1], minsLeft)]
                    builtRobot = True

            if robots[2] < maxObs:
                if robots[1] > 0:
                    # Work towards building an obsidian robot
                    timeNeeded = 1
                    oreNeeded = blueprint[2][0] - resources[0]
                    clyNeeded = blueprint[2][1] - resources[1]
                    if oreNeeded > 0 or clyNeeded > 0:
                        timeNeeded += max(ceil(oreNeeded/robots[0]), ceil(clyNeeded/robots[1]))
                    minsLeft = mins - timeNeeded
                    if minsLeft > 0:
                        queue += [(resources+(robots*timeNeeded)-blueprint[2], robots+newRobot[2], minsLeft)]
                        builtRobot = True

            if robots[2] > 1:
                # Work towards building a geode robot
                timeNeeded = 1
                oreNeeded = blueprint[3][0] - resources[0]
                obsNeeded = blueprint[3][2] - resources[2]
                if oreNeeded > 0 or obsNeeded > 0:
                    timeNeeded += max(ceil(oreNeeded/robots[0]), ceil(obsNeeded/robots[2]))
                minsLeft = mins - timeNeeded
                if minsLeft > 0:
                    queue += [(resources+(robots*timeNeeded)-blueprint[3], robots+newRobot[3], minsLeft)]
                    builtRobot = True

            if not builtRobot:
                # No robots are worth building
                geodes = resources[3] + (mins*robots[3])
                if geodes > maxGeodes:
                    maxGeodes = geodes

        del queue[0]

    print(f"Max geodes: {maxGeodes}")
    # totalQuality += (i+1)*maxGeodes
    productQuality *= maxGeodes
    print(f"Took {round(time.time()-start, 2)} seconds")
    print()

# print(f"Total quality: {totalQuality}")
print(f"Product quality: {productQuality}")