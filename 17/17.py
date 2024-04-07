#Advent of Code 2018: Day 17
import re
from collections import deque, namedtuple, defaultdict
from icecream import ic

def draw_underground(underground, min_row, max_row, min_col, max_col):
    for r in range(min_row-2, max_row+3):
        for c in range(min_col-2, max_col +3):
            print(underground[(r,c)], end="")
        print(" ")
    print(" ")

def generate_underground(lines):
    underground = defaultdict(lambda:".")
    for line in lines:
        m,n,o = map(int,(re.findall(r"\d+",line)))
        if line.startswith("x"):
            c1 = c2 = m #vertical line has column coord the same
            r1 = n
            r2 = o
        else:
            r1 = r2 = m #horizontal line has row coord the same
            c1 = n
            c2 = o
        for c in range(c1, c2 + 1):
            for r in range(r1, r2 + 1):
                underground[r,c] = "#"
    min_row = min(underground.keys(), key=lambda item: item[0])[0]
    max_row = max(underground.keys(), key=lambda item: item[0])[0]
    min_col = min(underground.keys(), key=lambda item: item[1])[1]
    max_col = max(underground.keys(), key=lambda item: item[1])[1]
    return underground, min_row, max_row, min_col, max_col

def spread_to_sides(drop):
    new_drops = []
    for i in [-1, +1]: #-1 = spread left, +1 = spread right
        row, col = drop.coord
        while underground[(row,col + i)] != "#":
            underground[(row,col + i)] = "~"
            if underground[(row+1, col+i)] == ".":
                new_drops.append(Drop((row, col+i), "d"))
                break
            col += i
    if len(new_drops) == 0:
        row, col = drop.coord
        new_drops.append(Drop((row-1,col), "s"))
    return new_drops

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

underground, min_row, max_row, min_col, max_col = generate_underground(lines)

Drop = namedtuple("Drop", ["coord", "dir"]) #direction: d=down, s=left+right
queue = deque([Drop((0,500), "d")])

while queue:
    current = queue.popleft()
    r,c = current.coord
    if r > max_row:
        continue
    if current.dir == "d": #drop down
        if underground[(r+1,c)] == ".": #space beneath - drop
            queue.append(Drop((r+1,c), "d"))
        if underground[(r+1,c)] == "#": #wall - spread left + righ
            queue.append(Drop((r,c), "s"))
    if current.dir == "s":
        new_drops = spread_to_sides(current)
        for new_drop in new_drops:
            queue.append(new_drop)
    underground[current.coord] = "~"
    ic(queue)
draw_underground(underground, min_row, max_row, min_col, max_col)

counter = 0
for coord, value in underground.items():
    if coord[0] >= min_row and value == "~":
        counter += 1

print(counter)

#TODO: Not working, minor issues - see test2.txt