#Advent of Code 2018: Day 6
from collections import Counter

def manhDistance(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

#MAIN:
with open("data.txt") as file:
    lines = file.read().splitlines()

coordinates = []
for line in lines:
    coordinates.append(tuple(int(x) for x in line.split(", ")))
x_min = min([point[0] for point in coordinates])
y_min = min([point[0] for point in coordinates])
x_max = max([point[0] for point in coordinates])
y_max = max([point[0] for point in coordinates])

locations = {}
counter = 0

for y in range(y_min, y_max+1):
    for x in range(x_min, x_max+1):
        distance = [manhDistance((x,y), point) for point in coordinates]
        closestPointIndex = distance.index(min(distance))
        if distance.count(distance[closestPointIndex]) > 1:
            winner = -1 #pokud je nejnizsi vzdalenost bodu k vice nez jednomu budu, bod se nebude pocitat
        else:
            winner = closestPointIndex
        locations.setdefault((x,y), winner)

        #podminka pro task2: pokud je suma manh dist od vsech bodu mensi nez 10000
        if sum(distance) < 10000:
            counter += 1

# pokud je hranicni bod nejblize nejakemu bodu, znamena to, ze se rozsiruje do nekonecna
# tento bod je potreba vyloucet
border = set()
for x in range(x_min, x_max):
    border.add(locations[x, y_min])
    border.add(locations[x, y_max])
for y in range(y_min, y_max):
    border.add(locations[x_min, y])
    border.add(locations[x_max, y])

#vycisti seznam vzdalenosti o body, ktere jsou na okrajich
cleanDistances = {}
for item in Counter(locations.values()):
    if item not in border:
        cleanDistances.setdefault(item, Counter(locations.values())[item])

print("Task 1:",max(cleanDistances.values()))
print("Task 2:", counter)