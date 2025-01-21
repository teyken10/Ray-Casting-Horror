import pygame
from bin.settings import *
from bin.map import world_map


xn = 0
yn = 0
def ray_casting(sc, player_pos, player_angle):
    global xn, yn
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_pos
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            # pygame.draw.line(sc, DARKGRAY, player_pos, (x, y), 2)
            # c = 255 / (1 + depth * depth * 0.0001)
            c = 255 / (1 + depth * depth * 0.0001)
            cell = (x // TILE * TILE, y // TILE * TILE)
            # Отрисовка стен
            if cell in world_map['W']:
                depth *= math.cos(player_angle - cur_angle)
                if depth != 0:
                    proj_height = PROJ_COEFF / depth
                else:
                    x = xn
                    y = yn
                    break
                color = (c // 3, c, c // 2)
                pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                xn = xo
                yn = yo
                break

            if cell in world_map['S']:
                depth *= math.cos(player_angle - cur_angle)
                if depth != 0:
                    proj_height = PROJ_COEFF / depth
                else:
                    x = xn
                    y = yn
                    break
                color = (c, c // 3, c // 2)
                pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                xn = xo
                yn = yo
                break

            if cell in world_map['D']:
                depth *= math.cos(player_angle - cur_angle)
                if depth != 0:
                    proj_height = PROJ_COEFF / depth
                else:
                    x = xn
                    y = yn
                    break
                color = (c // 2, c // 3, c)
                pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
                xn = xo
                yn = yo
                break
        cur_angle += DELTA_ANGLE
