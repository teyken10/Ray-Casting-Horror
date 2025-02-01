import math

import pygame
from bin.settings import settings
from bin.map import world_map, WORLD_WIDTH, WORLD_HEIGHT

tile = settings.tile


def mapping(a, b):
    return (a // tile) * tile, (b // tile) * tile


def ray_casting(player, textures):
    walls = []
    ox, oy = player.pos
    texture_v, texture_h = '1', '1'
    xm, ym = mapping(ox, oy)
    cur_angle = player.angle - settings.half_fov
    for ray in range(settings.num_rays):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        # пересечение с вертикалями
        x, dx = (xm + tile, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WORLD_WIDTH, tile):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * tile

        # пересечение с горизонталями
        y, dy = (ym + tile, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, WORLD_HEIGHT, tile):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * tile

        # проекция
        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % tile
        depth *= math.cos(player.angle - cur_angle)
        depth = max(depth, 0.00001)
        proj_height = min(int(settings.proj_coeff / depth), settings.penta_height)

        wall_column = textures[texture].subsurface(offset * settings.texture_scale, 0, settings.texture_scale,
                                                   settings.texture_height)
        wall_column = pygame.transform.scale(wall_column, (settings.scale, proj_height))
        wall_pos = (ray * settings.scale, settings.half_height - proj_height // 2)

        walls.append((depth, wall_column, wall_pos))
        cur_angle += settings.delta_angle
    return walls
