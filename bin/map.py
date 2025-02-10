from bin.settings import settings
import pygame

tile = settings.tile

with open('resources/maps/first_floor.txt', 'r', encoding='utf-8') as f:
    first_floor = [row.rstrip() for row in f.readlines()]

with open('resources/maps/second_floor.txt', 'r', encoding='utf-8') as f:
    second_floor = [row.rstrip() for row in f.readlines()]

WORLD_WIDTH = len(first_floor[0]) * tile
WORLD_HEIGHT = len(first_floor) * tile
world_map = {}
collision_walls = []
_ = False

def load_map(floor):
    for j, row in enumerate(floor):
        for i, char in enumerate(row):
            if char:
                collision_walls.append(pygame.Rect(i * tile, j * tile, tile, tile))
                if char == '1':
                    world_map[(i * tile, j * tile)] = '1'
                elif char == '2':
                    world_map[(i * tile, j * tile)] = '2'
                elif char == '3':
                    world_map[(i * tile, j * tile)] = '3'
                elif char == '4':
                    world_map[(i * tile, j * tile)] = '4'
    return [collision_walls, world_map]
