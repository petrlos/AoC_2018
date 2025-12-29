#Advent of Code 2018: Day 24
import re
from icecream import ic
import time

class Unit:
    def __init__(self, which_army, line, group_id):
        self.group_id = group_id
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
        self.selected = False
        self.target = None
        self.theor_dmg = 0

    @property
    def eff_power(self):
        return self.count * max(self.dmg_given)

    def __repr__(self):
        return f"Army {which[self.which_army]} {self.group_id}: Units: {self.count}"

def all_dead(armies):
    immune = []
    infection = []
    for army in armies:
        if army.which_army == 0: immune.append(army.count)
        elif army.which_army == 1: infection.append(army.count)
    if sum(immune) == 0: return False
    if sum(infection) == 0: return False
    return True

#MAIN
with open("data.txt") as file:
    lines = file.read().split("\n")

dmg_type = dict(zip("fire,cold,slashing,radiation,bludgeoning".split(","), (range(5))))
which = dict({0: "Immune", 1: "Infect"})

armies = []
which_army = 0
group_id = 1
for line in lines[1:]:
    if line == "": continue
    if "Infection" in line:
        which_army += 1
        group_id = 1
        continue
    unit = Unit(which_army, line, group_id)
    armies.append(unit)
    group_id += 1

while all_dead(armies):
    #sort via decreasing efficient power, by tie by initiative
    armies.sort(key=lambda g: (-g.eff_power, -g.init))
    #find target
    for attacker in armies:
        if attacker.count == 0: continue
        attacker.target = None #initialize
        attacker.theor_dmg = -1
        for target in armies:
            if target.selected: continue
            if attacker.which_army == target.which_army: continue
            if target.count == 0: continue
            theor_dmg = max([x*y*attacker.count for x, y in zip(attacker.dmg_given, target.weaknesses)])
            if attacker.target is None: #did not find any target
                attacker.target = target
                attacker.theor_dmg = theor_dmg
            #target found - compare by dmg, by effective power, by initiative
            elif ((theor_dmg, target.eff_power, target.init) >
                    (attacker.theor_dmg, attacker.target.eff_power,attacker.target.init)):
                attacker.target = target
                attacker.theor_dmg = theor_dmg
        if attacker.target is not None: attacker.target.selected = True

    #sort by initiative
    armies.sort(key=lambda g: (-g.init))
    #attack
    for attacker in armies:
        if attacker.count == 0: continue #all dead
        if attacker.target is None: continue
        dmg_done = max([x*y*attacker.count for x, y in zip(attacker.dmg_given, attacker.target.weaknesses)])
        kills = min(attacker.target.count, dmg_done // attacker.target.hp)
        #print(f"{which[attacker.which_army]} {attacker.group_id}: deals {dmg_done} to group {attacker.target.group_id} and kills {kills} units.")
        attacker.target.count -= kills

    for army in armies:
        army.target = None
        army.selected = False

immune = []
infection = []
for army in armies:
    if army.which_army == 0: immune.append(army.count)
    elif army.which_army == 1: infection.append(army.count)
print("Immune:", sum(immune))
print("Infection:", sum(infection))