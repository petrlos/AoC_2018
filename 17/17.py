#Advent of Code 2018: Day 17
import re
from collections import namedtuple, defaultdict

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

def drop_down(drop):
    to_be_filled = set()
    new_drops = []
    r,c = drop.coord
    while underground[(r + 1, c)] in "." and not r > max_row:
        r += 1
        to_be_filled.add((r,c))
        if underground[(r + 1, c)] in "~#":
            new_drops.append(Drop((r, c), "s"))
            return new_drops, to_be_filled # "bottom" to be filled - either hard, or water
    return [], to_be_filled #  toplayer of filled reservoir

def spread_to_sides(drop):
    to_be_filled = {drop.coord}
    new_drops = []
    for i in [-1, +1]: #-1 = spread left, +1 = spread right
        row, col = drop.coord
        while underground[(row,col + i)] != "#": #look left + right as long as border found
            to_be_filled.add((row, col+i))
            if underground[(row+1, col+i)] == ".":
                new_drops.append(Drop((row, col+i), "d"))
                break
            col += i
    if len(new_drops) == 0:
        water_type = "~" #in reservoir - will be filled with layer above
        row, col = drop.coord
        new_drops.append(Drop((row-1,col), "s"))
    else:
        water_type = "|" #top layer
    return new_drops, water_type, to_be_filled

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

underground, min_row, max_row, min_col, max_col = generate_underground(lines)

Drop = namedtuple("Drop", ["coord", "dir"]) #direction: d=down, s=left+right
queue = [(Drop((0,500), "d"))]

while queue:
    current = queue.pop()
    if current.dir == "d": #drop down
        new_drops, to_be_filled = drop_down(current)
        water_type = "|"
    else: #else is only "s" - spread to sides
        new_drops, water_type, to_be_filled = spread_to_sides(current)
    underground.update({filled: water_type for filled in to_be_filled})
    queue += new_drops

part1 = part2 = 0
for coord, value in underground.items():
    if max_row >= coord[0] >= min_row:
        if value in "|~": # each drop
            part1 += 1
        if value == "~": # drops in reservoirs only
            part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)