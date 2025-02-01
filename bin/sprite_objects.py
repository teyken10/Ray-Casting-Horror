import math

import pygame
from bin.settings import settings

tile = settings.tile


class Sprites:
    def __init__(self):
        self.sprite_types = {
            'table': pygame.image.load('resources/sprites/table.png').convert_alpha(),
            'devil': [pygame.image.load(f'resources/sprites/devil/{i}.png').convert_alpha() for i in range(8)]
        }
        self.list_of_objects = [
            SpriteObject(self.sprite_types['table'], True, (15.9, 5.1), 2, 0.4),
            SpriteObject(self.sprite_types['table'], True, (15.9, 4.1), 2, 0.4),
            SpriteObject(self.sprite_types['devil'], False, (10, 6), -0.2, 2)
        ]


class SpriteObject:
    def __init__(self, object, static, pos, shift, scale):
        self.object = object
        self.static = static
        self.pos = self.x, self.y = pos[0] * tile, pos[1] * tile
        self.shift = shift
        self.scale = scale

        if not static:
            self.sprite_angles = [frozenset(range(i, i + 45)) for i in range(0, 360, 45)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}

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

        fake_ray = current_ray + settings.fake_rays
        if 0 <= fake_ray <= settings.fake_rays_range and distance_to_sprite > 30:
            proj_height = min(int(settings.proj_coeff / distance_to_sprite * self.scale), settings.double_height)
            half_proj_height = proj_height // 2
            shift = half_proj_height * self.shift

            if not self.static:
                if theta < 0:
                    theta += settings.double_pi
                theta = 360 - int(math.degrees(theta))

                for angles in self.sprite_angles:
                    if theta in angles:
                        self.object = self.sprite_positions[angles]
                        break

            sprite_pos = (
            current_ray * settings.scale - half_proj_height, settings.half_height - half_proj_height + shift)
            sprite = pygame.transform.scale(self.object, (proj_height, proj_height))
            return (distance_to_sprite, sprite, sprite_pos)
        else:
            return (False,)
