#Advent of Code 2018: Day 22

def getErosion(geologicalIndex, depth):
    return (geologicalIndex + depth) % 20183

def generateErosions(target, depth):
    map = {}
    map.setdefault((0,0), getErosion(0, depth))
    xMax = 1
    while target not in map.keys():
        for x in range(xMax, -1, -1):
            y = xMax - x
            if x == 0:
                geologicalIndex = y * 48271
            elif y == 0:
                geologicalIndex = x * 16807
            else:
                geologicalIndex = map[x-1, y] * map[x, y-1]
            erosion = getErosion(geologicalIndex, depth)
            map.setdefault((x,y), erosion)
        xMax += 1
    map[target] = getErosion(0, depth) #coordinates of target have geologicalIndex = 0
    return map

def getRiskLvl(target, depth):
    erosions = generateErosions(target, depth)
    riskLvl = 0
    for y in range(target[1]+1):
        for x in range(target[0]+1):
           riskLvl += erosions[(x,y)] % 3
    return riskLvl

#MAIN:
test = getRiskLvl((10,10), 510)
print("Test data, should be 114:",test)

task1 = getRiskLvl((10,785), 5616)
print("Task1:", task1)