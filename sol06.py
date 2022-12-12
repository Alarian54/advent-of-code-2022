# Parsing
file = open('../data/data6.txt', 'r')
data = file.read()
file.close()
lines = data.split("\n")

# Part 1
line = lines[0]
i = 0
while True:
    seq = line[i:i+4]
    if len(seq)==len(set(seq)):
        print(i+4)
        break
    i += 1 

# Part 2
i = 0
while True:
    seq = line[i:i+14]
    if len(seq)==len(set(seq)):
        print(i+14)
        break
    i += 1 