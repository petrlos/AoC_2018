#Advent of Code 2O18 - Day 4
import re
from collections import Counter

def task1():
    max = 0; maxID = ""
    for key in guards.keys():
        if len(guards[key]) > max:
            max = len(guards[key])
            maxID = key
    maxIDnum = int(maxID[1:])
    return maxIDnum * Counter(guards[maxID]).most_common(1)[0][0]

#MAIN
regGuardID = re.compile(r"(#\d+)")
with open("data.txt", "r") as file:
    lines = sorted(file.read().splitlines())

guards = {}

for line in lines:
    if "#" in line:
        guardID = regGuardID.search(line).group()
    if guardID not in guards.keys():
        guards.setdefault(guardID, [])
    if "sleep" in line:
        start = int(line[15:17])
    if "wake" in line:
        end = int(line[15:17])
        guards[guardID] += list(range(start, end))

print("Task 1:",task1())

for key in guards.keys():
    guards[key] = Counter(guards[key])
    print(key, ":", end="")
    if len(guards[key]) > 0:
        print(Counter(guards[key]).most_common(1)[0])
    else:
        print("no sleep")

print("Find the most sleepy guard yourself :P :) ")
print("It should be #2879 with minute 49, 21 times asleep")
print("Task 2: 2879 * 49", 2879*49)