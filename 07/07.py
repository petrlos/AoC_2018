#Advent of Code 2018 Day 07

with open("data.txt", "r") as file:
    lines = file.read().replace("Step ", "").replace(" must be finished before step ", "").\
        replace(" can begin.", "").splitlines()

order = ""

while lines.count("##") < len(lines):
    possibleCandidate = set()
    firstLetters = [x[0] for x in lines]
    secondLetters = [x[1] for x in lines]
    for letter in firstLetters:
        if letter not in secondLetters:
            possibleCandidate.add(letter)
    if len(possibleCandidate) == 1:
        sortedOut = list(possibleCandidate)[0]
    else:
        sortedOut = sorted(list(possibleCandidate))[0]
    for index, line in enumerate(lines):
        if sortedOut in line:
            lastOne = line[1]
            lines[index] = "##"

    order += sortedOut
order += lastOne

print("Task 1:",order)