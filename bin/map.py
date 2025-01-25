from bin.settings import settings

''' S - STAIR, D - DOOR, W - WALL, . - FREE SPACE, T - tHIRD FLOOR, P - player'''
with open('resources/maps/first_floor.txt', 'r', encoding='utf-8') as f:
    first_floor = [row.rstrip() for row in f.readlines()]
# print(first_floor)
#
# with open('resources/maps/second_floor.txt', 'r', encoding='utf-8') as f:
#     second_floor = [row.rstrip() for row in f.readlines()]


x_player = y_player = 0
# world_map = {
#     'W': set(),
#     'D': set(),
#     'S': set(),
#     'T': set()
# }
# for j, row in enumerate(first_floor):
#     for i, char in enumerate(row):
#         if char == 'P':
#             x_player = i * settings.tile
#             y_player = j * settings.tile
#         elif char != '.' and char != 'P':
#             world_map[char].add((i * settings.tile, j * settings.tile))


text_map = [
    '111111111111',
    '1......1...1',
    '1..111...1.1',
    '1....1..11.1',
    '1..2....1..1',
    '1..2...111.1',
    '1....1.....1',
    '1111111111111'
]

world_map = {}
mini_map = set()
for j, row in enumerate(first_floor):
    for i, char in enumerate(row):
        if char != '.':
            mini_map.add((i * settings.map_tile, j * settings.map_tile))
            if char == 'W':
                world_map[(i * settings.tile, j * settings.tile)] = 'W'
            elif char == 'D':
                world_map[(i * settings.tile, j * settings.tile)] = 'D'
