with open ('input3.txt', 'r') as reader:
    myList =[l for l in reader.read().split('\n')]

def problem1(myMap):
    pointer=0
    treeCount=0
    for line in myMap:
        if line[pointer%len(line)]=="#":
            treeCount+=1
        pointer+=3
    return treeCount

def problem2(myMap):
    product = 1
    slopes={"slope1":{"moveRight":1, "moveDown":1, "treeCount":0}, "slope2":{"moveRight":3, "moveDown":1, "treeCount":0},
        "slope3":{"moveRight":5, "moveDown":1, "treeCount":0}, "slope4":{"moveRight":7, "moveDown":1, "treeCount":0},
        "slope5":{"moveRight":1, "moveDown":2, "treeCount":0}}
    for slope in slopes:  
        lineCount=0
        pointer=0
        while lineCount < len(myMap):
            if myMap[lineCount][pointer % len(myMap[lineCount])]=="#":
                slopes[slope]["treeCount"]+=1
            pointer+= slopes[slope]["moveRight"]
            lineCount+=slopes[slope]["moveDown"]
        product *= slopes[slope]["treeCount"]
    return product

print(problem1(myList))
print(problem2(myList))
