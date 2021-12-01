#Advent of Code 2018: Day 18 - Game Of Life - tuple, coords, dict
import copy
from datetime import datetime
start = datetime.now()

def tupleSum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def getNeighbours(midPoint):
    neighbours = ""
    for coords in neighCoords:
        possibleNeighbourKey = tupleSum(coords, midPoint)
        if possibleNeighbourKey in grid.keys():
            neighbours += grid[possibleNeighbourKey]
    return neighbours

#MAIN:

neighCoords = [(-1,1), (-1,0), (-1,-1), (0,1), (0,-1), (1,1), (1,0), (1,-1)]

with open("data.txt") as file:
    lines = file.read().splitlines()

grid = {}
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        grid.setdefault((x,y), char)
#gridSize je nejvyssi dosazena hodnota x a y
gridSizeX = x; gridSizeY = y

open = "."; tree = "|"; lumberyard = "#"

gridStates = []
for counter in range(10):
    newGrid = {}
    for key in grid.keys():
        neighbours = getNeighbours(key)
        if grid[key] == open:
            if neighbours.count(tree) >= 3:
                newGrid.setdefault(key, tree)
            else:
                newGrid.setdefault(key, grid[key])
        elif grid[key] == tree:
            if neighbours.count(lumberyard) >= 3:
                newGrid.setdefault(key, lumberyard)
            else:
                newGrid.setdefault(key, grid[key])
        elif grid[key] == lumberyard:
            if neighbours.count(lumberyard) >= 1 and neighbours.count(tree) >= 1:
                newGrid.setdefault(key, lumberyard)
            else:
                newGrid.setdefault(key, open)

    """    if newGrid not in gridStates:
        gridStates.append(newGrid)
    else:
        print("GOT YOU", counter)
    """

    grid = copy.deepcopy(newGrid)

#task1:
result = "".join(list(grid.values()))
print("Task 1:", result.count(tree) * result.count(lumberyard))
print("Runtime:",datetime.now()-start)

#task2:
print("Task 2: ", 176782)
#od 505. iterace je pole stabilni, na overeni zrusit komentov z line 54-58
# + na line 34 nastavit hodnotu 510+