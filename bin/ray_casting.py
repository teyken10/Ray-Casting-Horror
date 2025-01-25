import math

import pygame
from bin.settings import settings
from bin.map import world_map

# xn = 0
# yn = 0
# def ray_casting(sc, player_pos, player_angle):
#     global xn, yn
#     cur_angle = player_angle - settings.half_fov
#     xo, yo = player_pos
#     for ray in range(settings.num_rays):
#         sin_a = math.sin(cur_angle)
#         cos_a = math.cos(cur_angle)
#         for depth in range(settings.max_depth):
#             x = xo + depth * cos_a
#             y = yo + depth * sin_a
#             # pygame.draw.line(sc, settings.darkgray, player_pos, (x, y), 2)
#             c = 255 / (1 + depth * depth * 0.00001)
#             cell = (x // settings.tile * settings.tile, y // settings.tile * settings.tile)
#             # Отрисовка стен
#             if cell in world_map['W']:
#                 depth *= math.cos(player_angle - cur_angle)
#                 if depth != 0:
#                     proj_height = settings.proj_coeff / depth
#                 else:
#                     x = xn
#                     y = yn
#                     break
#                 color = (c // 3, c, c // 2)
#                 pygame.draw.rect(sc, color, (ray * settings.scale, settings.half_height - proj_height // 2, settings.scale, proj_height))
#                 xn = xo
#                 yn = yo
#                 break
#
#             if cell in world_map['S']:
#                 depth *= math.cos(player_angle - cur_angle)
#                 if depth != 0:
#                     proj_height = settings.proj_coeff / depth
#                 else:
#                     x = xn
#                     y = yn
#                     break
#                 color = (c, c // 3, c // 2)
#                 pygame.draw.rect(sc, color, (ray * settings.scale, settings.half_height - proj_height // 2, settings.scale, proj_height))
#                 xn = xo
#                 yn = yo
#                 break
#
#             if cell in world_map['D']:
#                 depth *= math.cos(player_angle - cur_angle)
#                 if depth != 0:
#                     proj_height = settings.proj_coeff / depth
#                 else:
#                     x = xn
#                     y = yn
#                     break
#                 color = (c // 2, c // 3, c)
#                 pygame.draw.rect(sc, color, (ray * settings.scale, settings.half_height - proj_height // 2, settings.scale, proj_height))
#                 xn = xo
#                 yn = yo
#                 break
#         cur_angle += settings.delta_angle

tile = settings.tile


def mapping(a, b):
    return (a // tile) * tile, (b // tile) * tile


def ray_casting(screen, player_pos, player_angle, textures):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - settings.half_fov
    for ray in range(settings.num_rays):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        # пересечение с вертикалями
        x, dx = (xm + tile, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, settings.width, tile):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * tile

        # пересечение с горизонталями
        y, dy = (ym + tile, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, settings.height, tile):
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
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth, 0.00001)
        proj_height = min(int(settings.proj_coeff / depth), 2 * settings.height)

        wall_column = textures[texture].subsurface(offset * settings.texture_scale, 0, settings.texture_scale, settings.texture_height)
        wall_column = pygame.transform.scale(wall_column, (settings.scale, proj_height))
        screen.blit(wall_column, (ray * settings.scale, settings.half_height - proj_height // 2))

        cur_angle += settings.delta_angle
