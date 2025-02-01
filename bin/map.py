from bin.settings import settings

with open('resources/maps/first_floor.txt', 'r', encoding='utf-8') as f:
    first_floor = [row.rstrip() for row in f.readlines()]
# print(first_floor)
#
# with open('resources/maps/second_floor.txt', 'r', encoding='utf-8') as f:
#     second_floor = [row.rstrip() for row in f.readlines()]

WORLD_WIDTH = len(first_floor[0]) * settings.tile
WORLD_HEIGHT = len(first_floor) * settings.tile
world_map = {}
mini_map = set()
_ = False
for j, row in enumerate(first_floor):
    for i, char in enumerate(row):
        if char:
            if char == '1':
                world_map[(i * settings.tile, j * settings.tile)] = '1'
            elif char == '2':
                world_map[(i * settings.tile, j * settings.tile)] = '2'
            elif char == '3':
                world_map[(i * settings.tile, j * settings.tile)] = '3'
