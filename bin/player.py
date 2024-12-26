from bin.settings import *
import pygame
import math


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.last_mouse_pos_x = None

    @property
    def pos(self):
        return (self.x, self.y)

    def mouse_motion(self, pos_x):
        if self.last_mouse_pos_x:
            if self.last_mouse_pos_x > pos_x:
                self.angle -= rotate_speed
                self.last_mouse_pos_x = pos_x

            elif self.last_mouse_pos_x < pos_x:
                self.angle += rotate_speed
                self.last_mouse_pos_x = pos_x

        else:
            self.last_mouse_pos_x = pos_x

        if pos_x[0] < WIDTH // 80 or pos_x[0] > WIDTH - WIDTH // 80:
            pygame.mouse.set_pos(HALF_WIDTH, HALF_HEIGHT)
        # print(self.last_mouse_pos_x)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pygame.K_q]:
            self.angle -= rotate_speed * 2
        if keys[pygame.K_e]:
            self.angle += rotate_speed * 2
