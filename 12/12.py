#Advent of Code 2018 Day 12
def prepareState(state):
    return "..." + state[2:-2] + "..."

def findIndexes(state):
    return [i-offset for i, char in enumerate(state) if char == "#"]

#MAIN
with open("data.txt", "r") as file:
    lines = file.read().splitlines()

offset = 10000

state = "#.#..#..###.###.#..###.#####...########.#...#####...##.#....#.####.#.#..#..#.#..###...#..#.#....##."

instructions = {}
for line in lines:
    lineSplit = line.split(" => ")
    instructions.setdefault(lineSplit[0], lineSplit[1])

state = "."*offset + state + "."*offset
for cycle in range(20):
    state = prepareState(state)
    newState = ""
    for i in range(0, len(state)-4):
        cutOf = state[i:i+5]
        if cutOf in instructions.keys():
            newState += instructions[cutOf]
        else:
            newState += "."
    state = prepareState(newState)

print("Task 1:", sum(findIndexes(state)))

print("Task 2: 3,650,000,000,377")
#od cisla 160 je kazdy dalsi prirustek vzdy +73, tzn. vysledek je:
# (5G - 160) *73 + prirustek na 160