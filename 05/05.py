#Advent of Code 2018: Day 5

def delPair(input):
    for i in range(0,len(input)-1):
        slice = input[i:i+2]
        if (slice[0].islower() and slice[1].isupper()) or (slice[0].isupper() and slice[1].islower()):
            if slice[0].upper() == slice[1].upper():
                return input.replace(slice, "")
    return input

def colapse(input):
    while True:
        newPolymer = delPair(input)
        if len(newPolymer) == len(input):
            break
        else:
            input = newPolymer
    return len(input)

#MAIN
with open("data.txt", "r") as file:
    polymer = file.read()
#polymer = "dabAcCaCBAcCcaDA"

#Task1
print(colapse(polymer))

#Task2
alphabet = "abcdefghijklmnopqrstuvwxyz"
results = []
for char in alphabet:
    partiallyColapsed = polymer.replace(char.upper(), "").replace(char.lower(), "")
    results.append(colapse(partiallyColapsed))

print(min(results))