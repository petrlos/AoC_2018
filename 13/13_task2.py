#AoC 2018 Day 13: Cart class

class Cart:
    def __init__(self, x,y, direction):
        self.coords = (x,y)
        self.coordsIndex = y * 10000 + x
        self.direction = direction
        self.directionIndex = 0
        self.alive = True

    def getCoordsIndex(self):
        x,y = self.coords
        self.coordsIndex = y * 10000  + x

from collections import Counter

def tupleSum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def killAllCartsOnCoords(coords):
    for cartie in carts:
        if cartie.coords == coords:
            cartie.alive = False

def cartsRemaining():
    restCartCounter = 0
    for littleCart in carts:
        if littleCart.alive:
            restCartCounter += 1
    return restCartCounter

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
restCartCounter = cartsRemaining()

while restCartCounter > 1:
    counter += 1
    #sort carts by coords - lefttop first, rightbottom last
    carts.sort(key = lambda x: x.coordsIndex, reverse = False)
    #move carts
    for cart in carts:
        if cart.alive:
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

            #check if there are some collisions
            locations = []
            for littleCart in carts:
                if littleCart.alive:
                    if littleCart.coords not in locations:
                        locations.append(littleCart.coords)
                    else:
                        killAllCartsOnCoords(littleCart.coords)
            restCartCounter = cartsRemaining()

for cart in carts:
    if cart.alive:
        print("Task 2 - last cart standing on coords: ",cart.coords)