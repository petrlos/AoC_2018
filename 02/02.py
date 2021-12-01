#Advent of Code 2018: Day 02
def findDuplet(word):
    for char in alphabet:
        if (char*2 in word) and (char*3 not in word):
            return True
    return False

def findTriplet(word):
    for char in alphabet:
        if char*3 in word:
            return True
    return False

def compare(word1, word2):
    result = ""
    difference = 0
    for char1, char2 in zip(word1, word2):
        if char1 != char2:
            difference += 1
        else:
            result += char1
    if difference == 1:
        print(result)

#MAIN
with open("data.txt", "r") as file:
    boxCodes = file.read().splitlines()

alphabet = "abcdefghijklmnopqrstuvwxyz"

duplets = 0
triplets = 0
for code in boxCodes:
    word = "".join(sorted(code))
    if findDuplet(word):
        duplets +=1
    if findTriplet(word):
        triplets += 1

for index1, word1 in enumerate(boxCodes):
    for index2, word2 in enumerate(boxCodes):
        if index1 != index2:
            compare(word1, word2)


print("Task 1:", duplets*triplets)