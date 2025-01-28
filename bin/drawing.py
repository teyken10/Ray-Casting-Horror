import math
import pygame
from bin.settings import settings
from bin.ray_casting import ray_casting
from bin.map import mini_map


class Drawing:
    def __init__(self, screen, screen_map):
        self.screen = screen
        self.sc_map = screen_map
        self.font = pygame.font.Font('resources/main_font.ttf', settings.width // 40)
        self.textures = {'W': pygame.image.load('resources/textures/wall.png').convert(),
                         'D': pygame.image.load('resources/textures/door.png').convert(),
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

    def mini_map(self, player):
        self.sc_map.fill(settings.black)
        map_x, map_y = player.x // settings.map_scale, player.y // settings.map_scale
        pygame.draw.line(self.sc_map, settings.yellow, (map_x, map_y),
                         (map_x + 12 * math.cos(player.angle), map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, settings.red, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, settings.sandy, (x, y, settings.map_tile, settings.map_tile))
        self.screen.blit(self.sc_map, settings.map_pos)
