#Advent of Code 2018 Day 03
import re

regNum = re.compile(r"\d+")

with open("data.txt", "r") as file:
    claims = file.read().splitlines()

fabric = {}

for claim in claims:
    numbers = [int(x) for x in regNum.findall(claim)]
    start = [numbers[1], numbers[2]]; size = [numbers[3], numbers[4]]
    for x in range(start[0], start[0] + size[0]):
        for y in range(start[1], start[1] + size[1]):
            if (x,y) in fabric.keys():
                fabric[x,y] += 1
            else:
                fabric.setdefault((x,y), 1)

#Get all claims
task1 = len(list(filter(lambda x: x>1, fabric.values())))
print("Task 1", task1)

#Check all claimes
for claim in claims:
    numbers = [int(x) for x in regNum.findall(claim)]
    start = [numbers[1], numbers[2]]; size = [numbers[3], numbers[4]]
    pieceOfCloth = []
    for x in range(start[0], start[0] + size[0]):
        for y in range(start[1], start[1] + size[1]):
            pieceOfCloth.append(fabric[(x,y)])
    if len(pieceOfCloth) == sum(pieceOfCloth):
        result = numbers[0]
print("Task 2", result)