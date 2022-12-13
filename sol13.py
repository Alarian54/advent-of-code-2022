# Setup
file = open('../data/data13.txt', 'r')
data = file.read()
file.close()
lines = data.split("\n")
pairs = (len(lines)+1)//3

def makeList(line):
    if line=="[]": return []
    if line.isnumeric(): return int(line)
    line = line[1:-1]
    if line.isnumeric(): return [int(line)]
    list1 = []
    i = 0
    while i<len(line):
        if line[i]=="[":
            start = i
            brackets = 1
            while brackets>0:
                i += 1
                if line[i]=="[": brackets += 1
                if line[i]=="]": brackets -= 1
            i += 1
            elem = makeList(line[start:i])
            list1 += [elem]
        elif line[i].isnumeric():
            start = i
            string = line[i]
            repeat = True
            while repeat:
                if i<len(line):
                    if line[i].isnumeric(): i += 1
                    else: repeat = False
                else: repeat = False
            elem = int(line[start:i])
            list1 += [elem]
        i += 1
    return list1

def getFirst(packet1, packet2):
    i = 0
    while i<min(len(packet1), len(packet2)):
        val1, val2 = packet1[i], packet2[i]
        if isinstance(val1, int) and isinstance(val2, int):
            if int(val1)<int(val2): return "correct"
            if int(val1)>int(val2): return "incorrect"
        elif isinstance(val1, list) and isinstance(val2, list):
            answer = getFirst(val1, val2)
            if "correct" in answer: return answer
        else:
            if isinstance(val1, int): answer = getFirst([val1], val2)
            else: answer = getFirst(val1, [val2])
            if "correct" in answer: return answer
        i += 1
    if len(packet1)<len(packet2): return "correct"
    if len(packet1)>len(packet2): return "incorrect"
    else: return "neither"

# Part 1
totalIndex = 0
for i in range(pairs):
    packet1 = eval(lines[3*i])
    packet2 = eval(lines[(3*i)+1])
    first = getFirst(packet1, packet2)
    if first=="correct": totalIndex += (i+1)
print(totalIndex)

# Part 2
packetGroups = [[[[2]]], [[[6]]]]
for i in range(pairs):
    packetGroups += [[makeList(lines[3*i])]]
    packetGroups += [[makeList(lines[(3*i)+1])]]

while len(packetGroups)>1:
    mergedGroups = []
    i = 0
    while i<len(packetGroups):
        if i==(len(packetGroups)-1):
            mergedGroups += [packetGroups[-1]]
            i += 1
        else:
            packetGroup1 = packetGroups[i]
            packetGroup2 = packetGroups[i+1]
            mergedGroup = []
            j, k = 0, 0
            while j<len(packetGroup1) and k<len(packetGroup2):
                packet1 = packetGroup1[j]
                packet2 = packetGroup2[k]
                if getFirst(packet1, packet2)=="correct":
                    mergedGroup += [packet1]
                    j += 1
                else:
                    mergedGroup += [packet2]
                    k += 1
            if j==len(packetGroup1): mergedGroup += packetGroup2[k:]
            else: mergedGroup += packetGroup1[j:]
            mergedGroups += [mergedGroup]
            i += 2
    packetGroups = mergedGroups
packetGroups = packetGroups[0]

i = 0
decoderKey = 1
while i<len(packetGroups):
    if packetGroups[i]==[[2]] or packetGroups[i]==[[6]]:
        decoderKey *= (i+1)
    i += 1
print(decoderKey)
