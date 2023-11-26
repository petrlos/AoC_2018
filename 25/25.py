#Advent of Code 2018: Day 25
import re

def parseData(lines):
    regNum = re.compile(r"-?\d+")
    points = []
    for line in lines:
        #converts list of strings to list of ints
        points.append(list(map(int,regNum.findall(line))))
    return points

def manhDistance(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

#MAIN
with open("test.txt") as file:
    lines = file.read().splitlines()

points = parseData(lines)

##TODO: not working - some points may join smaller groups into larger group -> total count is too high

groups = [ [points[0]] ]
for point in points:
    pointGroupFound = False
    for group in groups[:]:
        for groupPoint in group[:]:
            if manhDistance(point, groupPoint) <=3:
                group.append(point)
                pointGroupFound = True
    if not pointGroupFound:
        groups.append([point])

print(len(groups))
for group in groups:
    print(group)