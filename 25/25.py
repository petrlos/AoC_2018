#Advent of Code 2018: Day 25
from datetime import datetime
timer_start = datetime.now()

def check_distance(coord, constellations):
    #check for already checked coords in which constellations is MD <= 3
    where = list()
    for id, constellation in enumerate(constellations):
        for coord_checked in constellation:
            if manh_distance(coord_checked, coord) <= 3:
                where.append(id)
    return where

def merge_constellations(constellations, where, coord):
    new_constellations = []
    merged = set()
    merged.add(tuple(coord))
    for wh in where:
        merged = merged | (constellations[wh])
    for id, constellation in enumerate(constellations):
        if id not in where:
            new_constellations.append(set(constellation))
    new_constellations.append(merged)
    return new_constellations

def manh_distance(a, b): #universal function for manhattan distance, works in n-D space
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

#MAIN

with open("data.txt") as file:
    lines = file.read().splitlines()

coords = set(tuple(map(int, line.split(","))) for line in lines)

constellations = []

for coord in coords:
    where = check_distance(coord, constellations)
    if len(where) == 0: #no match found - create new constelation
        new_const = set()
        new_const.add(tuple(coord))
        constellations.append(new_const)
    elif len(where) == 1: #add to existing
        constellations[where[0]].add(coord)
    else: #merge
        constellations = merge_constellations(constellations, where, coord)

print("Part 1:", len(constellations))
print("Runtime:", datetime.now() - timer_start)