file = open('../data/data1.txt', 'r')
data = file.read()
file.close()
lines = data.split("\n")

# Part 1
calories = []
i, total = 0, 0
while i<len(lines):
    if lines[i]!="":
        total += int(lines[i])
    else:
        calories += [total]
        total = 0
    i += 1
print(max(calories))

# Part 2
total3 = 0
for i in range(3):
    maxCals = max(calories)
    maxCalsIndex = calories.index(maxCals)
    total3 += maxCals
    del calories[maxCalsIndex]
print(total3)