from bin.audio import Audio
from bin.settings import settings
import pygame
import math
from bin.map import world_map
from bin.ray_casting import mapping


class Player:
    def __init__(self):
        self.audio = Audio()
        self.x, self.y = settings.player_pos
        self.angle = settings.player_angle
        self.side = 50
        self.rect = pygame.Rect(*settings.player_pos, self.side, self.side)
        self.open_door_sound = self.audio.run_sound('resources/sounds/open_door.mp3', settings.volume_sound)
        self.can_open_door = True

    @property
    def pos(self):
        return (self.x, self.y)

    def detect_collision(self, dx, dy):
        if dx != 0:
            delta_x = (self.side // 2) * abs(dx) / dx
            fx1, fx2 = mapping(self.x + dx + delta_x, self.y + delta_x)
            sx1, sx2 = mapping(self.x + dx + delta_x, self.y - delta_x)
            if (fx1, fx2) in world_map:
                if world_map[(fx1, fx2)] == '1':
                    dx = 0
            if (sx1, sx2) in world_map:
                if world_map[(sx1, sx2)] == '1':
                    dx = 0
                    self.can_open_door = True
                if world_map[(sx1, sx2)] == '2' and self.can_open_door:
                    self.open_door_sound.play()
                    self.can_open_door = False
                else:
                    self.can_open_door = True
                if world_map[(sx1, sx2)] == '3':
                    settings.second_floor = True
                    settings.first_floor = False
                    self.can_open_door = True
        if dy != 0:
            delta_y = (self.side // 2) * abs(dy) / dy
            fy1, fy2 = mapping(self.x + delta_y, self.y + dy + delta_y)
            sy1, sy2 = mapping(self.x - delta_y, self.y + dy + delta_y)
            if (fy1, fy2) in world_map:
                if world_map[(fy1, fy2)] == '1':
                    dy = 0
            if (sy1, sy2) in world_map:
                if world_map[(sy1, sy2)] == '1':
                    dy = 0
        self.x += dx
        self.y += dy

    def get_key(self, d, value):
        for k, v in d.items():
            if v == value:
                return k

    def movement(self):
        self.keys_control()
        self.mouse_control()
        self.rect.center = self.x, self.y
        self.angle %= settings.double_pi

    def keys_control(self):
        player_speed = settings.player_speed
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx = player_speed * cos_a
            dy = player_speed * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_s]:
            dx = -player_speed * cos_a
            dy = -player_speed * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_a]:
            dx = player_speed * sin_a
            dy = -player_speed * cos_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_d]:
            dx = -player_speed * sin_a
            dy = player_speed * cos_a
            self.detect_collision(dx, dy)

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - settings.half_width
            pygame.mouse.set_pos((settings.half_width, settings.half_height))
            self.angle += difference * settings.sensitivity
