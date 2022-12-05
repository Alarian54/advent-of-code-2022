file = open('../data/data4.txt', 'r')
data = file.read()
file.close()
lines = data.split("\n")

# Part 1
total = 0
for line in lines:
    elf1, elf2 = line.split(",")
    start1, end1 = list(map(int, elf1.split("-")))
    start2, end2 = list(map(int, elf2.split("-")))
    if start1<=start2 and end1>=end2: total += 1
    elif start2<=start1 and end2>=end1: total += 1
print(total)

# Part 2
total = 0
for line in lines:
    elf1, elf2 = line.split(",")
    start1, end1 = list(map(int, elf1.split("-")))
    start2, end2 = list(map(int, elf2.split("-")))
    if end1>=start2 and end2>=start1: total += 1
print(total)