import pygame
from pygame.mixer_music import get_volume

from bin.drawing import Drawing
from bin.settings import *
from bin.player import Player
from bin.ray_casting import ray_casting
from bin.audio import Audio
# from bin.map import x_player, y_player, world_map
from bin.map import world_map


# from bin.map import world_map


class Game:
    def __init__(self, main_menu):
        self.audio = Audio()
        # self.lobby_music = self.audio.run_music("resources/lobby_music.mp3", settings.volume_music / 100)
        self.main_menu = main_menu

    def run(self):
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        pygame.init()
        screen = pygame.display.set_mode((settings.width, settings.height))
        sc_map = pygame.Surface((settings.width // settings.map_scale, settings.height // settings.map_scale))
        clock = pygame.time.Clock()
        # player = Player(player_pos=(x_player, y_player))
        player = Player()
        drawing = Drawing(screen, sc_map)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False  # Выход из игры

                if event.type == pygame.MOUSEMOTION:
                    player.mouse_motion(event.pos)

                else:
                    player.last_mouse_pos_x = (settings.width // 2, settings.height // 2)

            player.movement()
            screen.fill(settings.black)


            drawing.background(player.angle)
            drawing.world(player.pos, player.angle)
            drawing.fps(clock)
            # drawing.mini_map(player)

            # pygame.draw.circle(screen, settings.green, (int(player.x) // 7, int(player.y) // 7), 12)
            # pygame.draw.line(screen, settings.green, player.pos, (player.x // 7 + settings.width * math.cos(player.angle),
            #                                                       player.y // 7 + settings.width * math.sin(player.angle)), 2)
            #
            # for x, y in world_map:
            #     pygame.draw.rect(screen, settings.darkgray, (x // 7, y // 7, settings.tile // 7, settings.tile // 7), 2)

            pygame.display.flip()
            clock.tick(settings.fps)

        pygame.mouse.set_visible(True)
        pygame.event.set_grab(False)

        # Возвращаемся к главному меню
        self.main_menu.lobby_music.play(-1)
