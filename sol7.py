# Parsing
file = open('../data/data7.txt', 'r')
data = file.read()
file.close()
lines = data.split("\n")
lines += ["$"]

# Defining objects
class Node:
    def __init__(self, name, directory=False, parent=None, size=0):
        self.name = name
        self.directory = directory
        self.parent = parent
        self.size = size
        self.children = None

    def __str__(self):
        return self.name

    def getName(self):
        return self.name

    def getDirectory(self):
        return self.directory

    def getParent(self):
        return self.parent

    def getChildren(self):
        return self.children
    
    def addChild(self, child):
        if self.children == None:
            self.children = [child]
        else:
            self.children += [child]

    def getSize(self):
        if self.getDirectory():
            total = 0
            if self.children != None:
                for child in self.getChildren():
                    total += child.getSize()
            return total
        else:
            return self.size

    def print(self):
        print(self.name)
        for child in self.getChildren():
            child.print()
root = Node("/", directory = True)

# Part 1
currentNode = None
i = 0
while i<(len(lines)-1):
    if lines[i] == "$ cd /":
        currentNode = root
        i += 1

    elif lines[i][0:4] == "$ cd":
        if lines[i] == "$ cd ..":
            currentNode = currentNode.getParent()
        else:
            for node in currentNode.getChildren():
                if node.getName() == lines[i][5:]:
                    currentNode = node
        i += 1

    elif lines[i] == "$ ls":
        i += 1
        while lines[i][0] != "$":
            if lines[i].split(" ")[0] == "dir":
                newNode = Node(name = lines[i].split(" ")[1], directory = True, parent=currentNode)
                currentNode.addChild(newNode)
            else:
                newNode = Node(name = lines[i].split(" ")[1], parent=currentNode, size=int(lines[i].split(" ")[0]))
                currentNode.addChild(newNode)
            i += 1

global total
total = 0
def addSizes(node):
    if node.getDirectory():
        size = node.getSize()
        if size<100000:
            global total
            total += size
        if node.getChildren != None:
            children = node.getChildren()
            for child in children:
                addSizes(child)
                
addSizes(root)
print(total)

# Part 2
unusedSpace = 70000000 - root.getSize()
global spaceRequired
spaceRequired = 30000000 - unusedSpace

global minSize
minSize = 70000000
def findMin(node):
    if node.getDirectory():
        size = node.getSize()
        global spaceRequired
        global minSize
        if size>=spaceRequired and size<minSize:
            minSize = size
        if node.getChildren != None:
            children = node.getChildren()
            for child in children:
                findMin(child)

findMin(root)
print(minSize)