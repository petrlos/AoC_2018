#Advent of Code 2018: Day 8
#answer should be 40746

class Node:
    def __init__(self, num_children, num_metadata):
        self.num_children = num_children
        self.num_metadata = num_metadata
        self.children = []
        self.metadata = []

def parse_tree(numbers):
    #vezme z celeho listu prvni dve pozice - pocet deti a pocet metadat
    child_count, metadata_count = numbers.pop(0), numbers.pop(0)
    #zalozi instanci tridy Node
    node = Node(child_count, metadata_count)
    #pokud je pocet deti vetsi nez 0, zavola funkci opet se zkracenym listem
    for _ in range(child_count):
        node.children.append(parse_tree(numbers))
    #do metadat ulozi prvnich "metadata_count" cisel a orizne list
    for _ in range(metadata_count):
        node.metadata.append(numbers.pop(0))
    return node

#MAIN
with open("test.txt") as file:
    numbers = list(map(int,file.read().split(" ")))

tree = parse_tree(numbers)

print(" ")