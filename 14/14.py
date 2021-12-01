#Advent of Code 2018: Day 14

elfOnePosition = 0
elfTwoPosition = 1

recipes = "37"
desiredLength = 652601

#part1
while len(recipes) < 10 + desiredLength:
    toBeAdded = int(recipes[elfOnePosition]) + int(recipes[elfTwoPosition])
    if toBeAdded >= 10:
        recipes += "1"
    recipes += str(toBeAdded % 10)
    elfOnePosition = (int(recipes[elfOnePosition]) + 1 + elfOnePosition) % len(recipes)
    elfTwoPosition = (int(recipes[elfTwoPosition]) + 1 + elfTwoPosition) % len(recipes)
print("Task 1:", recipes[-10:])

elfOnePosition = 0
elfTwoPosition = 1

recipes = "37"
while str(desiredLength) not in recipes[-10:]:
    toBeAdded = int(recipes[elfOnePosition]) + int(recipes[elfTwoPosition])
    if toBeAdded >= 10:
        recipes += "1"
    recipes += str(toBeAdded % 10)
    elfOnePosition = (int(recipes[elfOnePosition]) + 1 + elfOnePosition) % len(recipes)
    elfTwoPosition = (int(recipes[elfTwoPosition]) + 1 + elfTwoPosition) % len(recipes)
result = len(recipes) - len(str(desiredLength))

#pokud recepty nekonci na pozadovanou sekvenci, cela sekvence je o 1 znak delsi, je potreba odecist jednicku
if not recipes.endswith(str(desiredLength)):
    result -= 1
print("Task 2:",result)