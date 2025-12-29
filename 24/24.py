#Advent of Code 2018: Day 24
import re
from icecream import ic

class Unit:
    def __init__(self, which_army, line):
        self.which_army = which_army
        self.count = int(re.search(r"(\d+) units", line).group(1))
        self.hp = int(re.search(r"(\d+) hit", line).group(1))
        dmg, dtype = re.search(r"(\d+) (\w+) damage", line).groups()
        self.dmg_given = [0] * 5
        self.dmg_given[dmg_type[dtype]] = int(dmg)
        self.init = int(re.search(r"initiative (\d+)", line).group(1))
        weak = []
        immune = []
        if "(" in line:
            weaknesses = re.search(r"\(([^0-9()]*)\)", line).group(1)
            for weakness in weaknesses.split("; "):
                if "immune" in weakness:
                    immune = [dmg_type[x] for x in weakness.replace("immune to ", "").split(", ")]
                elif "weak" in weakness:
                    weak = [dmg_type[x] for x in weakness.replace("weak to ", "").split(", ")]
        self.weaknesses = [0 if i in immune else 2 if i in weak else 1 for i in range(5)]
        self.dmg_taken = 0

    @property
    def eff_power(self):
        return self.count * max(self.dmg_given)

    def __repr__(self):
        which = dict({0: "Immune:", 1: "Infect:"})
        return f"Type: {which[self.which_army]} Units:{self.count}, HP:{self.hp}, Init.:{self.init}, Weak.:{self.weaknesses}, Dmg.:{self.dmg_given}"

#MAIN
with open("data.txt") as file:
    lines = file.read().split("\n")

dmg_type = dict(zip("fire,cold,slashing,radiation,bludgeoning".split(","), (range(5))))
armies = []
which_army = 0
for line in lines[1:]:
    if line == "": continue
    if "Infection" in line:
        which_army += 1
        continue
    unit = Unit(which_army, line)
    print(unit)
    armies.append(unit)

ic(armies)