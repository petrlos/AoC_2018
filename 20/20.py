#Advent of Code 2018: Day 20
from collections import deque

def tupleSum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def generateMaze(regexPath):
    directions = {"W":(-1,0), "E":(1,0), "N":(0,1), "S":(0,-1)}
    maze = {(0,0):"X"}
    currentPosition = (0,0)
    lastInterception = []
    for char in regexPath:
        if char in directions.keys():
            currentPosition = tupleSum(currentPosition, directions[char])
            maze[currentPosition] = "+" # door
            currentPosition = tupleSum(currentPosition, directions[char])
            maze[currentPosition] = "."
        elif char == "(":
            lastInterception.append(currentPosition)
        elif char == "|":
            currentPosition = lastInterception[-1]
            lastInterception = lastInterception[:-1]

    return maze

def printMaze(maze):
    lstX, lstY = [], []
    for x,y in maze.keys():
        lstX.append(x)
        lstY.append(y)
    for y in range(max(lstY)+1, min(lstY)-2, -1):
        for x in range(min(lstX)-1, max(lstX)+2, 1):
            if (x, y) in maze.keys():
                print(maze[(x, y)], end="")
            else:
                print("#", end="")
        print(" ")

def bfs(maze):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    distances = {(0,0):0}
    queue = deque([(0,0)])
    while queue:
        currentPoint = queue[0]
        for direction in directions:
            neighbourDoor = tupleSum(direction, currentPoint)
            if neighbourDoor in maze.keys():
                notVisitedRoom = tupleSum(neighbourDoor, direction)
                if notVisitedRoom not in distances.keys():
                    distances[notVisitedRoom] = distances[currentPoint] + 1
                    queue.append(notVisitedRoom)
        queue.popleft()
    return max(distances.values())

#MAIN
with open("test.txt") as file:
    lines = file.read().splitlines()

print("Results should be: 10, 18, 23 and 31 for test mazes:")
for regexPath in lines:
    maze = generateMaze(regexPath)
    result = bfs(maze)
    print("Maze: {0}: maxDist: {1}".format(regexPath, result))

with open("data.txt") as file:
    lines = file.read().splitlines()

maze = generateMaze(lines[0])
result = bfs(maze)
print("Result Task1:", result)