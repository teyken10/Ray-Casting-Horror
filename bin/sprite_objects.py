import math
import pygame
from bin.settings import settings
from collections import deque

tile = settings.tile


class Sprites:
    def __init__(self):
        self.sprite_parameters = {
            'sprite_devil': {
                'sprite': pygame.image.load('resources/sprites/devil/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': -0.2,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'resources/sprites/devil/anim/{i}.png').convert_alpha() for i in range(9)]),
                'animation_dist': 800,
                'animation_speed': 15,
                # 'blocked': True
            },

            'sprite_table': {
                'sprite': pygame.image.load('resources/sprites/table/base/0.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 2.5,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'resources/sprites/table/base/0.png').convert_alpha()]),
                'animation_dist': 800,
                'animation_speed': 15,
                # 'blocked': True
            }
        }
        self.sprite_types = {
            'table': pygame.image.load('resources/sprites/table/base/0.png').convert_alpha(),
            'devil': [pygame.image.load(f'resources/sprites/devil/base/{i}.png').convert_alpha() for i in range(8)]
        }
        self.list_of_objects = [
            SpriteObject(self.sprite_parameters['sprite_devil'], (5, 15)),
            SpriteObject(self.sprite_parameters['sprite_devil'], (30, 35)),
            # SpriteObject(self.sprite_parameters['sprite_table'], (20, 3)),
            # SpriteObject(self.sprite_parameters['sprite_table'], (20, 4.5)),
            # SpriteObject(self.sprite_parameters['sprite_table'], (20, 6)),
            # SpriteObject(self.sprite_parameters['sprite_table'], (18, 3)),
            # SpriteObject(self.sprite_parameters['sprite_table'], (18, 4.5)),
            # SpriteObject(self.sprite_parameters['sprite_table'], (18, 6)),
        ]


class SpriteObject:
    def __init__(self, parameters, pos):
        self.object = parameters['sprite']
        self.viewing_angles = parameters['viewing_angles']
        self.shift = parameters['shift']
        self.scale = parameters['scale']
        self.animation = parameters['animation']
        self.animation_dist = parameters['animation_dist']
        self.animation_speed = parameters['animation_speed']
        self.animation_count = 0
        self.pos = self.x, self.y = pos[0] * tile, pos[1] * tile
        if self.viewing_angles:
            self.sprite_angles = [frozenset(range(i, i + 45)) for i in range(0, 360, 45)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}

    def object_locate(self, player):
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
            # выбор спрайта для угла
            if self.viewing_angles:
                if theta < 0:
                    theta += settings.double_pi
                theta = 360 - int(math.degrees(theta))

                for angles in self.sprite_angles:
                    if theta in angles:
                        self.object = self.sprite_positions[angles]
                        break

            # анимация спрайта
            sprite_object = self.object
            if self.animation and distance_to_sprite < self.animation_dist:
                sprite_object = self.animation[0]
                if self.animation_count < self.animation_speed:
                    self.animation_count += 1
                else:
                    self.animation.rotate()
                    self.animation_count = 0

            # размер и позиция спрайта
            sprite_pos = (
                current_ray * settings.scale - half_proj_height, settings.half_height - half_proj_height + shift)
            sprite = pygame.transform.scale(sprite_object, (proj_height, proj_height))
            return (distance_to_sprite, sprite, sprite_pos)
        else:
            return (False,)
