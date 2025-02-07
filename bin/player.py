from bin.settings import settings
import pygame
import math
from bin.map import world_map
from bin.ray_casting import mapping


class Player:
    def __init__(self):
        self.x, self.y = settings.player_pos
        self.angle = settings.player_angle
        self.side = 50
        self.rect = pygame.Rect(*settings.player_pos, self.side, self.side)

    @property
    def pos(self):
        return (self.x, self.y)

    def detect_collision(self, dx, dy):
        if dx != 0:
            delta_x = (self.side // 2) * abs(dx) / dx
            if mapping(self.x + dx + delta_x, self.y + delta_x) in world_map:
                dx = 0
            if mapping(self.x + dx + delta_x, self.y - delta_x) in world_map:
                dx = 0
        if dy != 0:
            delta_y = (self.side // 2) * abs(dy) / dy
            if mapping(self.x + delta_y, self.y + dy + delta_y) in world_map:
                dy = 0
            if mapping(self.x - delta_y, self.y + dy + delta_y) in world_map:
                dy = 0
        self.x += dx
        self.y += dy

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
