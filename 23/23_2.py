#Advent of Code 2018: Day 23
import re
from datetime import datetime
time_start = datetime.now()

def beacon_in_reach(beacon, cube_midpoint, step):
    #function generated via ChatGPT
    #returns if a cube with "midpoint" and size of "step" is in reach of a beacon
    bx, by, bz, beacon_range = beacon
    cx, cy, cz = cube_midpoint

    half_side = step // 2
    x_min, x_max = cx - half_side, cx + half_side
    y_min, y_max = cy - half_side, cy + half_side
    z_min, z_max = cz - half_side, cz + half_side

    nearest_x = max(x_min, min(bx, x_max))
    nearest_y = max(y_min, min(by, y_max))
    nearest_z = max(z_min, min(bz, z_max))

    manhattan_distance = abs(bx - nearest_x) + abs(by - nearest_y) + abs(bz - nearest_z)

    return manhattan_distance <= beacon_range

def get_new_midpoint(start, step, beacons):
    mul = 2
    midpoints = dict()
    x_s, y_s, z_s = start
    for x in range(x_s - mul*step, x_s + mul*step + 1, step):
        for y in range(y_s - mul*step, y_s + mul*step + 1, step):
            for z in range(z_s - mul*step, z_s + mul+step + 1, step):
                midpoints[(x, y, z)] = []

    for beacon in beacons:
        for midpoint, value in midpoints.items():
            if beacon_in_reach(beacon, midpoint, step):
                midpoints[midpoint].append(beacon)

    max_matches = max([len(length) for length in midpoints.values()])
    for midpoint, beacons_matching in midpoints.items():
        if len(beacons_matching) == max_matches:
            return midpoint

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

beacons = set()
for line in lines:
    numbers = tuple(map(int, (re.findall(r"-?\d+", line))))
    beacons.add(numbers)

midpoint = (0,0,0) #start in the middle
step = 2 ** 30

while step != 0:
    print(f"Cube size: {step}")
    midpoint = (get_new_midpoint(midpoint, step, beacons))
    for var, char in zip(midpoint, ["x", "y", "z"]):
        print(f"{char}: {var - step:_}, {var + step:_}")
    step = step // 2
    print(" ")
print("Result coords:", midpoint)
print("Result:", sum(midpoint))

print(datetime.now() - time_start)