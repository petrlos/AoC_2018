#Advent of Code 2018: Day 23
import re

def manhattanDistance(strongestBot, bot):
    distance = 0
    for i in range(0,3):
        distance += abs(strongestBot[i] - bot[i])
    return distance

regNum = re.compile(r"-?\d+")

with open("data.txt") as file:
    lines = file.read().splitlines()

bots = {}
for line in lines:
    numbers = [int(x) for x in regNum.findall(line)]
    bots.setdefault((numbers[0], numbers[1], numbers[2]), numbers[3])

#find strongest bot
largestSignal = max(bots.values())
for bot in bots.keys():
    if bots[bot] == largestSignal:
        strongestBot = bot

reachable = []
for bot in bots:
    distance = manhattanDistance(strongestBot, bot)
    if distance <= bots[strongestBot]:
        reachable.append(bot)

print("Task1:",len(reachable))

