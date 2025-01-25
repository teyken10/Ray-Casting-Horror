from bin.settings import settings
import pygame
import math


class Player:
    # def __init__(self, player_pos=(0, 0)):
    def __init__(self):
        self.x, self.y = settings.player_pos
        self.angle = settings.player_angle
        self.last_mouse_pos_x = None

    @property
    def pos(self):
        return (self.x, self.y)

    def mouse_motion(self, pos_x):
        if self.last_mouse_pos_x:
            if self.last_mouse_pos_x > pos_x:
                self.angle -= settings.rotate_speed
                self.last_mouse_pos_x = pos_x

            elif self.last_mouse_pos_x < pos_x:
                self.angle += settings.rotate_speed
                self.last_mouse_pos_x = pos_x

        else:
            self.last_mouse_pos_x = pos_x

        if pos_x[0] < settings.width // 80 or pos_x[0] > settings.width - settings.width // 80:
            pygame.mouse.set_pos(settings.half_width, settings.half_height)
        # print(self.last_mouse_pos_x)

    def movement(self):
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
        if keys[pygame.K_q]:
            self.angle -= settings.rotate_speed * 2
        if keys[pygame.K_UP]:
            settings.player_speed += 1
        if keys[pygame.K_DOWN] and settings.player_speed > 0:
            settings.player_speed -= 1
