#Advent of Code 2018 - Day 09
from collections import deque


def marbleGame(players, maxMarble):
    currentMarble = 2
    marbles = deque([0,2,1])
    highestScore = {}
    for i in range(players):
        highestScore.setdefault(str(i), 0)

    for i in range(3,maxMarble+1):
        if i % 23 == 0:
            currentPlayer = i % players
            highestScore[str(currentPlayer)] += i + marbles[-8]
            marbles.rotate(7)
            marbles.pop()
            currentMarble = marbles[0]
        else:
            while marbles[-2] != currentMarble:
                marbles.rotate(-1)
            marbles.append(i)
            currentMarble = i
    return highestScore

#MAIN

task1 = marbleGame(447,71510)
print("Task 1:",max(task1.values()))

task2 = marbleGame(447,71510*100)
print("Task 2:", max(task2.values()))

