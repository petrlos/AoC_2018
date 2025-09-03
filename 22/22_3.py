#Advent of Code 2018: Day 23
import heapq
from collections import defaultdict
from icecream import ic

class Cave:
    def __init__(self, depth, target):
        self.depth = depth
        self.erosion = dict()
        self.target = target

    def get_erosion(self, row, col):
        if (row, col) in self.erosion.keys():
            return self.erosion[(row, col)]
        else:
            if row == 0:
                geo_index = col * 48271
            elif col == 0:
                geo_index = row * 16807
            else:
                geo_index = self.get_erosion(row - 1, col) * self.get_erosion(row, col - 1)
            if (row, col) == self.target:
                geo_index = 0
            self.erosion[(row, col)] = (geo_index + self.depth) % 20183
            return self.erosion[(row, col)]
    def total_risk_lvl(self):
        risk_lvl = 0
        x_max, y_max = self.target
        for row in range(x_max + 1):
            for col in range(y_max + 1):
                risk_lvl += self.get_erosion(row, col) %3
        return risk_lvl

def find_path(cave):
    results = [float("inf")]
    possible_tools = {
        0: {+1, -1},  # rocky = torch, climbing
        1: {-1, 0},  # wet = climbing, nothing
        2: {+1, 0}  # narrow = torch, nothing
    }
    seen = defaultdict(lambda: float("inf"))
    seen[((0, 0), 1)] = 0  # (coords, tool): time
    queue = [(0, 0, 0, 0)] #time, tool, row, col
    heapq.heapify(queue)
    while queue:
        curr_time, curr_tool, curr_row, curr_col = heapq.heappop(queue)
        for new_row, new_col in [(curr_row+1, curr_col),
                                 (curr_row-1, curr_col),
                                 (curr_row, curr_col-1),
                                 (curr_row, curr_col+1)]:
            if new_row < 0 or new_col < 0: continue #out of border
            curr_terrain = cave.get_erosion(curr_row, curr_col) % 3
            new_terrain = cave.get_erosion(new_row, new_col) % 3
            if new_terrain != curr_terrain:
                new_tools = (possible_tools[curr_terrain] & possible_tools[new_terrain])
            else:
                new_tools = {curr_tool}
            if (new_row, new_col) == cave.target: #if target found
                if 1 in new_tools:
                    results.append(curr_time + 1) #torch in hand
                else:
                    results.append(curr_time + 8) #switch to torch
            for new_tool in new_tools:
                if new_tool == curr_tool:
                    new_time = curr_time + 1
                else:
                    new_time = curr_time + 7
                if seen[((new_row, new_col), new_tool)] > new_time:
                    seen[((new_row, new_col), new_tool)] = new_time
                    if new_time < min(results):
                        heapq.heappush(queue, (new_time, new_tool, new_row, new_col))
    return min(results)

#MAIN
test_cave = Cave(510, (10,10))
real_cave = Cave(5616, (10,785))

terrain = {0:".", 1:"=", 2:"|"}

print("Part 1 test:", test_cave.total_risk_lvl())
print("Part 1 real:", real_cave.total_risk_lvl())
print(" ")

print("Part 2 test:", find_path(test_cave))
print("Part 2 real:", find_path(real_cave))