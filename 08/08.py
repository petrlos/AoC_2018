#Advent of Code 2018 Day8:

#TODO: not yet working recursion

def getMetadata(numbers, children):
    currentPosition = 0
    if numbers[currentPosition] == 0: # neni potreba hledat vice do hloubky
        length = numbers[currentPosition+1]
        slice = numbers[currentPosition+2:currentPosition+2+length]
        currentPosition+= length + 2
        print(slice)
    else:
        for child in range(numbers[currentPosition]):
            getMetadata()

with open("test.txt") as file:
    data = file.readline()

#data = "0 3 1 2 3"
data = "1 1 0 99 2 1 1 2"
data = [int(x) for x in data.split(" ")]

print(data)

getMetadata(data, 1)