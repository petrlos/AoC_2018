#Advent of Code 2018: Day 22
from icecream import ic
import heapq
from collections import defaultdict

def get_erosion_lvl(row, col): #col = x, row = y
    if (row, col) in map_erosion.keys():
        return map_erosion[(row, col)]
    else:
        if row <= 0:
            geo_index = col * 16807
        elif col <= 0:
            geo_index = row * 48271
        else:
            geo_index = get_erosion_lvl(row - 1, col) * get_erosion_lvl(row, col - 1)
        if (row, col) == target:
            geo_index = 0
        map_erosion[(row, col)] = (geo_index + depth) % 20183
        return map_erosion[(row, col)]

def total_risk_lvl():
    risk_lvl = 0
    for col in range(target[0] + 1):
        for row in range(target[1] + 1):
            risk_lvl += get_erosion_lvl(row, col) % 3
    return risk_lvl

def manh_distance(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

#MAIN
map_erosion = dict()
test = False
if test:
    depth = 510
    target = (10,10)
else:
    depth = 5616
    target = (10, 785)

print("Part 1:", total_risk_lvl())

queue = [(0, (0, 0), 1)]  # time, coords, tool
heapq.heapify(queue)

possible_tools = {
    0: {+1, -1},  # rocky = torch, climbing
    1: {-1, 0},  # wet = climbing, nothing
    2: {+1, 0}  # narrow = torch, nothing
}
seen = defaultdict(lambda: float("inf"))
seen[((0, 0), 1)] = 0  # (coords, tool): time
result = -1

while queue:
    time, coords, tool = heapq.heappop(queue)
    row, col = coords
    terrain = get_erosion_lvl(row, col) % 3
    if coords == target and tool == 1:
        result = time
        break

    # dont move - change tool -> time += 7
    for new_tool in possible_tools[terrain]:
        if new_tool != tool:
            new_time = time + 7
            if seen[coords, new_tool] > new_time:
                seen[coords, new_tool] = new_time
                heapq.heappush(queue, (new_time, coords, new_tool))

    # move, dont change tool -> time += 1
    for new_row, new_col in [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)]:
        if new_row < 0 or new_col < 0: continue  # out of border
        new_time = time + 1
        new_terrain = get_erosion_lvl(new_row, new_col) % 3
        if tool not in possible_tools[new_terrain]: continue
        if seen[((new_row, new_col), tool)] > new_time:
            seen[((new_row, new_col), tool)] = new_time
            heapq.heappush(queue, (new_time, (new_row, new_col), tool))

ic(result, tool, coords)