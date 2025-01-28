import math

import pygame
from bin.settings import settings

tile = settings.tile


class Sprites:
    def __init__(self):
        self.sprite_types = {
            'table': pygame.image.load('resources/sprites/table.png').convert_alpha()
        }
        self.list_of_objects = [
            SpriteObject(self.sprite_types['table'], True, (10.1, 2.1), 1.8, 0.4),
            SpriteObject(self.sprite_types['table'], True, (15.9, 2.1), 1.8, 0.4),
        ]


class SpriteObject:
    def __init__(self, object, static, pos, shift, scale):
        self.object = object
        self.static = static
        self.pos = self.x, self.y = pos[0] * tile, pos[1] * tile
        self.shift = shift
        self.scale = scale

    def object_locate(self, player, walls):
        dx, dy = self.x - player.x, self.y - player.y
        distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += settings.double_pi

        delta_rays = int(gamma / settings.delta_angle)
        current_ray = settings.center_ray + delta_rays
        distance_to_sprite *= math.cos(settings.half_fov - current_ray * settings.delta_angle)

        if 0 <= current_ray < settings.num_rays - 1 and distance_to_sprite < walls[current_ray][0]:
            proj_height = int(settings.proj_coeff / distance_to_sprite + self.scale)
            half_proj_height = proj_height // 2
            shift = half_proj_height * self.shift

            sprite_pos = (
            current_ray * settings.scale - half_proj_height, settings.half_height - half_proj_height + shift)
            sprite = pygame.transform.scale(self.object, (proj_height, proj_height))
            return (distance_to_sprite, sprite, sprite_pos)
        else:
            return (False, False, False)
