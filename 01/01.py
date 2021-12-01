#Advent of Code 2018: Day 01

with open("data.txt", "r") as file:
    lines = [int(x) for x in file.read().splitlines()]

#Task1:
print("Task 1:",sum(lines))

checkSum = 0
checkSums = {0:None}
found = False
while not found:
    for number in lines:
        checkSum += number
        if checkSum not in checkSums.keys():
            checkSums.setdefault(checkSum, None)
        else:
            result = checkSum
            found =  True
        if found:
            break

print("Task 2:", result)