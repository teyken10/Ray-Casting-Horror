from bin.settings import *


''' S - STAIR, D - DOOR, W - WALL, . - FREE SPACE, T - tHIRD FLOOR, P - player'''
first_floor = []
with open('resources/maps/first_floor.txt', 'r', encoding='utf-8') as f:
    first_floor = [row.rstrip() for row in f.readlines()]
print(first_floor)

second_floor = []
with open('resources/maps/second_floor.txt', 'r', encoding='utf-8') as f:
    second_floor = [row.rstrip() for row in f.readlines()]

x_player = y_player = 0
world_map = {
    'W': set(),
    'D': set(),
    'S': set(),
    'T': set()
}
for j, row in enumerate(first_floor):
    for i, char in enumerate(row):
        if char == 'P':
            x_player = i * TILE
            y_player = j * TILE
        elif char != '.' and char != 'P':
            world_map[char].add((i * TILE, j * TILE))
