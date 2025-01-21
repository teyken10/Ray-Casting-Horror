import threading

import pygame
from bin.settings import *
from bin.player import Player
from bin.ray_casting import ray_casting
from bin.audio import Audio
from bin.map import x_player, y_player


class Game:
    def __init__(self, main_menu):
        self.audio = Audio()
        self.lobby_music = self.audio.run_music("resources/lobby_music.mp3", settings.volume_music / 100)
        self.main_menu = main_menu

    def run(self):
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()
        player = Player(player_pos=(x_player, y_player))

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
                    player.last_mouse_pos_x = (WIDTH // 2, HEIGHT // 2)

            player.movement()
            screen.fill(BLACK)

            pygame.display.set_caption(f'FPS: {math.trunc(clock.get_fps())}')

            pygame.draw.rect(screen, BLUE, (0, 0, WIDTH, HALF_HEIGHT))
            pygame.draw.rect(screen, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

            ray_casting(screen, player.pos, player.angle)

            pygame.display.flip()
            clock.tick(FPS)

        pygame.mouse.set_visible(True)
        pygame.event.set_grab(False)

        # Возвращаемся к главному меню
        self.main_menu.lobby_music.play(-1)
