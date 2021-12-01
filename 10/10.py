#Advent of Code 2018 Day 10
import re

def printScreen():
    screen = []
    for i in range(8):
        screen.append([" "] * 10)
    for point in points:
        screen[point[1]][point[0]] = "#"
    for line in screen:
        print("".join(line))

regNum = re.compile(r"-?\d+")

with open("test.txt", "r") as file:
    lines = file.read().splitlines()

points = []
velocities = []

for index, line in enumerate(lines):
    coords = [int(x) for x in regNum.findall(line)]
    points.append((coords[0], coords[1]))
    velocities.append((coords[2], coords[3]))

spread = []
for time in range(0,3):
    xmax = []
    for i in range(len(points)):
        xmax.append(points[i][0])
        points[i] = tuple(map(lambda x, y: x + y, points[i], velocities[i]))
    spread.append(max(xmax) - min(xmax))

printScreen()

#test working, solution via excel