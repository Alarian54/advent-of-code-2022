file = open('../data/data2.txt', 'r')
data = file.read()
file.close()
lines = data.split("\n")

# Part 1
score = 0
for line in lines:
    opp, me = line.split(" ")
    if me=="X":
        if opp=="A": score += 4
        if opp=="B": score += 1
        if opp=="C": score += 7
    if me=="Y":
        if opp=="A": score += 8
        if opp=="B": score += 5
        if opp=="C": score += 2
    if me=="Z":
        if opp=="A": score += 3
        if opp=="B": score += 9
        if opp=="C": score += 6
print(score)

# Part 2
score = 0
for line in lines:
    opp, me = line.split(" ")
    if me=="X":
        if opp=="A": score += 3
        if opp=="B": score += 1
        if opp=="C": score += 2
    if me=="Y":
        if opp=="A": score += 4
        if opp=="B": score += 5
        if opp=="C": score += 6
    if me=="Z":
        if opp=="A": score += 8
        if opp=="B": score += 9
        if opp=="C": score += 7
print(score)