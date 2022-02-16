#Advent of Code 2018: Day 16
import re
regNum = re.compile("\d+")

def checkOpcodes(before, opcodeLine, after):
    counter = 0
    opcodeNr, a, b, c = opcodeLine
    for opcode, func in opcodesLambdas.items():
        if after[c] == func(before, a, b):
            counter += 1
            opcodes[opcodeNr].add(opcode) #
    return counter >= 3

def lineToNum(line): #converts string "[1,2,3,4]" to list of int-numbers [1,2,3,4]
    return [int(x) for x in regNum.findall(line)]

def checkGroups(lines):
    groupsMatchThreeOpcodesCounter = 0
    for index in range(0, len(lines), 4):
        before, opcodeLine, after = lines[index:index + 3]
        if checkOpcodes(lineToNum(before), lineToNum(opcodeLine), lineToNum(after)):
            groupsMatchThreeOpcodesCounter += 1
    return groupsMatchThreeOpcodesCounter

def deleteOpcodes(opcodeNrLeave, opcodeToBeDeleted):
    opcodeToBeDeleted = list(opcodeToBeDeleted)[0]
    for opcodeNr, opcodeSet in opcodes.items():
        if opcodeNr != opcodeNrLeave:
            if opcodeToBeDeleted in opcodeSet:
                opcodes[opcodeNr].remove(opcodeToBeDeleted)

def decodeOpcodeNumbers(opcodes):
    allDone = False
    done = set()
    while not allDone:
        allDone = True
        for opcodeNr, opcode in opcodes.items():
            if len(opcode) > 1:
                allDone = False
            if len(opcode) == 1 and opcodeNr not in done:
                deleteOpcodes(opcodeNr, opcode)
                done.add(opcodeNr)
    #at this point each opcodeNr has only one string in set
    for i in range(16): #convert all sets with len == 1 to strings
        opcodes[i] = list(opcodes[i])[0]
    return opcodes

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

#definition of opcodes functions:
opcodesLambdas = {
    "addr": lambda before, a, b: before[a] + before[b],     #register + register
    "addi": lambda before, a, b: before[a] + b,             #register + value
    "mulr": lambda before, a, b: before[a] * before[b],     #register * register
    "muli": lambda before, a, b: before[a] * b,             #register * value
    "banr": lambda before, a, b: before[a] & before[b],     #register AND register
    "bani": lambda before, a, b: before[a] & b,             #register AND value
    "borr": lambda before, a, b: before[a] | before[b],     #register OR register
    "bori": lambda before, a, b: before[a] | b,             #register OR value
    "setr": lambda before, a, b: before[a],                 #set register
    "seti": lambda before, a, b: a,                         #set value
    "gtir": lambda before, a, b: a > before[b],             #value > register
    "gtri": lambda before, a, b: before[a] > b,             #register > value
    "gtrr": lambda before, a, b: before[a] > before[b],     #register > register
    "eqir": lambda before, a, b: a == before[b],            #value == register
    "eqri": lambda before, a, b: before[a] == b,            #register == value
    "eqrr": lambda before, a, b: before[a] == before[b],    #register == register
}

opcodes = dict()
for i in range(16):
    opcodes[i] = set()

#Task1:
print("Task 1:",checkGroups(lines))

#Task2
opcodesNr = decodeOpcodeNumbers(opcodes)
registers = [0,0,0,0]

with open("programm.txt") as file:
    lines = file.read().splitlines()

for index, line in enumerate(lines):
    opcode, a, b, c = lineToNum(line)
    registers[c] = opcodesLambdas[opcodesNr[opcode]](registers, a, b)

print("Task 2:", registers[0])