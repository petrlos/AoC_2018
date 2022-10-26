#Advent of Code 2018: Day 20
from collections import deque
import re

def tupleSum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def generateMaze(regexPath):
    directions = {"W":(-1,0), "E":(1,0), "N":(0,1), "S":(0,-1)}
    maze = {(0,0):"X"}
    currentPosition = (0,0) #start in the middle
    lastInterception = []
    for index, char in enumerate(regexPath):
        if char in directions.keys(): #move in desired direction
            currentPosition = tupleSum(currentPosition, directions[char])
            maze[currentPosition] = "+" #set up door
            currentPosition = tupleSum(currentPosition, directions[char])
            maze[currentPosition] = "." #set up room
        elif char == "(": #intersection - save position
            lastInterception.append(currentPosition)
        elif char == "|": #go to last interception
            currentPosition = lastInterception[-1]
        elif char == ")": #branch closed, remove interception from list
            lastInterception = lastInterception[:-1]
    return maze

def bfs(maze):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    distances = {(0,0):0}
    queue = deque([(0,0)])
    while queue: #bfs searchh
        currentPoint = queue[0]
        for direction in directions:
            neighbourDoor = tupleSum(direction, currentPoint)
            if neighbourDoor in maze.keys(): #is there a door in any direction?
                notVisitedRoom = tupleSum(neighbourDoor, direction) #in same direction must be a room as well
                if notVisitedRoom not in distances.keys(): #have i NOT yet visited this room?
                    distances[notVisitedRoom] = distances[currentPoint] + 1 #distance +1 to previous room
                    queue.append(notVisitedRoom) #must check neighbours of not yet visited rooms
        queue.popleft()
    task1 = max(distances.values())
    #task2: oneliner :)
    task2 = len(list(filter(lambda x: x >= 1000, distances.values())))
    return task1, task2

def countPath(line):
    maze = generateMaze(line)
    result = bfs(maze)
    return result

#MAIN
with open("test.txt") as file:
    lines = file.read().splitlines()

print("Test mazes: Results should be: 10, 18, 23 and 31:")
for line in lines:
    task1, task2 = countPath(line)
    print("Maze: {0}: maxDist: {1}".format(line, task1))

print(" ")
with open("data.txt") as file:
    lines = file.read().splitlines()

task1, task2 = countPath(lines[0])
print("Result Task1:", task1)
print("Result Task2:", task2)