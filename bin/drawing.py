import math
import pygame
from bin.settings import settings
from bin.ray_casting import ray_casting
from bin.map import mini_map


class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font('resources/fonts/main_font.ttf', settings.width // 40)
        self.textures = {'1': pygame.image.load('resources/textures/wall.png').convert(),
                         '2': pygame.image.load('resources/textures/door.png').convert(),
                         '3': pygame.image.load('resources/textures/up-stairs.png').convert(),
                         'S': pygame.image.load('resources/textures/sky.png').convert()
                         }

    def background(self, angle):
        sky_offset = -5 * math.degrees(angle) % settings.width
        self.screen.blit(self.textures['S'], (sky_offset, 0))
        self.screen.blit(self.textures['S'], (sky_offset - settings.width, 0))
        self.screen.blit(self.textures['S'], (sky_offset + settings.width, 0))
        pygame.draw.rect(self.screen, settings.darkgray,
                         (0, settings.half_height, settings.width, settings.half_height))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.screen.blit(object, object_pos)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, settings.red)
        self.screen.blit(render, settings.fps_pos)
