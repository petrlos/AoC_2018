#AoC 2018 Day 13: Cart class

class Cart:
    def __init__(self, x,y, direction):
        self.coords = (x,y)
        self.coordsIndex = y * 10000 + x
        self.direction = direction
        self.directionIndex = 0

    def getCoordsIndex(self):
        x,y = self.coords
        self.coordsIndex = y * 10000  + x

from collections import Counter

def tupleSum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

#MAIN

with open ("data.txt") as file:
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
            newCart = Cart(x,y,direction)
            carts.append(newCart)

collided = False
counter = 0
while not collided:
    counter += 1
    #sort carts by coords - righttop first, left bottom last
    carts.sort(key = lambda x: x.coordsIndex, reverse = False)
    #move carts
    for cart in carts:
        if tracks[cart.coords] == "\\":
            #turn on backslash
            cart.direction = backslash[cart.direction]
        elif tracks[cart.coords] == "/":
            #turn on slash
            cart.direction = slash[cart.direction]
        elif tracks[cart.coords] == "+":
            currentTurn = turn[cart.directionIndex]
            cart.direction = currentTurn[cart.direction]
            cart.directionIndex = (cart.directionIndex + 1) % 3
            #change direction
        cart.coords = tupleSum(cart.coords, cart.direction)
        cart.getCoordsIndex()
        #generate a list of all carts' locations
        locations = []
        for littleCart in carts:
            locations.append(littleCart.coords)
        #check if there are some collisions
        collisions = [x for x, y in Counter(locations).items() if y > 1]
        if len(collisions) > 0:
            print(collisions, counter)
            collided = True
