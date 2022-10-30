#Advent of Code 2018: Day 17
import re
from collections import defaultdict, Counter

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
        for x in range(494, 508):
            print(field[(x,y)], end="")
        print(" ")

def fillUpTheField(field, maxDepth):
    activePoints = {(500, 0)}
    while activePoints:
        for point in list(activePoints):
            x,y = point
            if field[(x,y+1)] == ".": #bellow active point no wall - drop
                activePoints.discard(point)
                if y+1 <= maxDepth:
                    field[(x,y+1)] = "~"
                    activePoints.add((x,y+1))

        drawField(field, maxDepth)
    return Counter(field.values())["~"]

#MAIN

with open("test2.txt") as file:
    lines = file.read().splitlines()

maxDepth, field = createField(lines)
#drawField(field, maxDepth)

result = fillUpTheField(field, maxDepth)
print("Total waterdrops filled:", result)