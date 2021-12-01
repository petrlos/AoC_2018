#Advent of Code 2018: Day 13
from collections import Counter

#TODO: Minecarts: test data work, normal not

def tupleSum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

#MAIN

with open ("test.txt") as file:
    lines = file.read().splitlines()

cartsChars = "^>v<"
up, right, down, left = (0,-1), (1,0), (0,1), (-1,0)
slash = {up: right, down: left, left: down, right: up}
backslash = {up:left, down:right, left:up, right:down}
turn = [
    {up: left, left: down, down: right, right: up},
    {up: up, left: left, right: right, down: down},
    {up: right, down:left, left: up, right: down}
]
carts = []; tracks = {}

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char in ["\\", "/", "-", "|", "+"]:
            tracks.setdefault((x,y), char)
        if char in cartsChars:
            if char == "<":
                direction = left
                tracks.setdefault((x,y), "-")
            elif  char == ">":
                direction = right
                tracks.setdefault((x,y), "-")
            elif char == "v":
                direction = down
                tracks.setdefault((x,y), "|")
            elif char == "^":
                direction = up
                tracks.setdefault((x, y), "|")
            newCart = [(x,y), direction, 0] #location, , rotation
            carts.append(newCart)

collided = False
counter = 0

while not collided:
    counter += 1
    locations = []
    for cart in carts:
        if tracks[cart[0]] == "\\":
            #turn on backslash
            cart[1] = backslash[cart[1]]
        elif tracks[cart[0]] == "/":
            #turn on slash
            cart[1] = slash[cart[1]]
        elif tracks[cart[0]] == "+":
            currentTurn = turn[cart[2]]
            cart[1] = currentTurn[cart[1]]
            cart[2] = (cart[2] + 1) % 3
            #change direction
        cart[0] = tupleSum(cart[0], cart[1])
        locations.append(cart[0])
    collisions = [x for x, y in Counter(locations).items() if y > 1]
    if len(collisions) > 0:
        print(collisions, counter)
        collided = True
