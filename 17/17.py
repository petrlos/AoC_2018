#Advent of Code 2018: Day 17
import re
from collections import defaultdict, Counter, deque

def createField(lines):
    def extendRangeList(interval):
        if len(interval) > 1:
            interval = list(range(interval[0], interval[1] + 1))
        return interval

    depths = []
    regNum = re.compile(r"\d+")
    field = defaultdict(lambda: ".")
    field[(500,0)] = "+"
    for line in lines:
        first, second = line.split(", ")
        x = extendRangeList(list(map(int,regNum.findall(first))))
        y = extendRangeList(list(map(int,regNum.findall(second))))
        if line[0] == "y": #switch horizontal/vertical lines
            x,y = y,x
        depths += y
        for xCoord in x:
            for yCoord in y:
                field[(xCoord,yCoord)] = "#"
    return max(depths), field

def drawField(field, maxDepth):
    print("  44444455555555")
    print("  99999900000000")
    print("  45678901234567")
    for y in range(0, maxDepth+2):
        print(str(y)[-1], end=" ")
        for x in range(1, 1000):
            print(field[(x,y)], end="")
        print(" ")

def fillUpTheField(field, maxDepth):
    activePoints = {(500, 0)}
    while activePoints:
        for point in list(activePoints):
            dropFound = False
            x,y = point
            if field[(x,y+1)] == ".": #bellow active point free space - drop
                if y+1 <= maxDepth:
                    field[(x,y+1)] = "~"
                    activePoints.add((x,y+1))
                activePoints.discard(point)
            else:
                offset = 1
                while field[(x-offset, y)] != "#": #look left and find a wall or a drop
                    field[(x-offset, y)] = "~"
                    if field[(x-offset), y+1] == ".":
                        activePoints.discard(point)
                        activePoints.add((x-offset, y))
                        dropFound = True
                        break
                    offset += 1
                offset = 1
                while field[(x+offset, y)] != "#": #look right and find a wall or a drop
                    field[(x+offset, y)] = "~"
                    if field[(x+offset), y+1] == ".":
                        activePoints.discard(point)
                        activePoints.add((x+offset, y))
                        dropFound = True
                        break
                    offset += 1
                if not dropFound:
                    activePoints.discard(point)
                    activePoints.add((x, y-1))
    return Counter(field.values())["~"]

#MAIN

#TODO: Test data working, data.txt not

with open("test.txt") as file:
    lines = file.read().splitlines()

maxDepth, field = createField(lines)
result = fillUpTheField(field, maxDepth)
drawField(field, maxDepth)

print("Total waterdrops filled:", result)