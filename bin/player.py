from bin.settings import settings
import pygame
import math


class Player:
    # def __init__(self, player_pos=(0, 0)):
    def __init__(self):
        self.x, self.y = settings.player_pos
        self.angle = settings.player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        self.keys_control()
        self.mouse_control()
        self.angle %= settings.double_pi

    def keys_control(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += settings.player_speed * cos_a
            self.y += settings.player_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -settings.player_speed * cos_a
            self.y += -settings.player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += settings.player_speed * sin_a
            self.y += -settings.player_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -settings.player_speed * sin_a
            self.y += settings.player_speed * cos_a

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - settings.half_width
            pygame.mouse.set_pos((settings.half_width, settings.half_height))
            self.angle += difference * settings.sensitivity
