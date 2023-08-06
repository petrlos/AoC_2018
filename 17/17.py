#Advent of Code 2018: Day 17
import re
from collections import defaultdict, Counter, deque

def create_field(lines):
    field = defaultdict(lambda: ".")
    for line in lines:
        constant, start, end = list(map(int, (re.findall(r"\d+", line))))
        list_constant = [constant] * (end-start+1)
        list_range = list(range(start, end+1))
        if line[0] == "x":
            coords = (zip(list_constant, list_range))
        else:
            coords = (zip(list_range, list_constant))
        for coord in coords:
            field[coord] = "#"
    return field

def draw_field(field):
    print("  44444455555555 \n  99999900000000 \n  45678901234567")
    for y in range(0, 14):
        print(str(y)[-1], end=" ")
        for x in range(494, 508):
                print(field[(x,y)], end="")
        print(" ")

#MAINd
with open("test.txt") as file:
    lines = file.read().splitlines()

field = create_field(lines)
draw_field(field)