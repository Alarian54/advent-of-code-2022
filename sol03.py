file = open('../data/data3.txt', 'r')
data = file.read()
file.close()
lines = data.split("\n")

chars = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Part 1
total = 0
for line in lines:
    half = len(line)//2
    comp1 = line[half:]
    comp2 = line[:half]
    for item in comp1:
        if item in comp2:
            common = item
    total += chars.index(common)
print(total)

# Part 2
total, i = 0, 0
common = ""
while i<len(lines):
    line1, line2, line3 = lines[i], lines[i+1], lines[i+2]
    for item in line1:
        if item in line2:
            if item in line3:
                common = item
    total += chars.index(common)
    i += 3
print(total)