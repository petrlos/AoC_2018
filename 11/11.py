#Advent of Code 2018 Day 11
from pprint import pprint as pp
def getMaxPowerInSquareInSizeOf(size):
    gridSquarePower = {}
    for y in range(1, 301 - size):
        for x in range(1, 301 - size):
            squarePower = getSquarePower(x, y, size)
            gridSquarePower.setdefault((x, y), squarePower)
    maxPower = max(gridSquarePower.values())
    for key in gridSquarePower.keys():
        if gridSquarePower[key] == maxPower:
            return key, maxPower

def getPowerLvl(x,y,serialNumber):
    powerLvlMultiplied = ((x + 10) * y + serialNumber) * (x + 10)
    hundredDigit = int(str(powerLvlMultiplied)[-3:-2])
    return hundredDigit - 5

def getSquarePower(startX,startY, size):
    powerLvls = []
    for y in range(startY,startY+size):
        for x in range(startX,startX+size):
            powerLvls.append(grid[(x,y)])
    return sum(powerLvls)

#MAIN
grid = {}
gridID = 5719

for y in range(1,301):
    for x in range(1,301):
        newPower = getPowerLvl(x,y,gridID)
        grid.setdefault((x,y), newPower)

#TASK1: Square size = 3
coords, maxPower = getMaxPowerInSquareInSizeOf(3)
print("Task 1:", coords)

#TASK2: get max power in different squaresizes
differentSquareSizeMax = {}
for size in range(15,18):
    print("Counting square size:", size)
    coords, maxPower = getMaxPowerInSquareInSizeOf(size)
    print("   max power: {1} at coords {0}".format(coords, maxPower))
    differentSquareSizeMax.setdefault(maxPower, [coords, size])

print("Task 2:",differentSquareSizeMax[max(differentSquareSizeMax.keys())])