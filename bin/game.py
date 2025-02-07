import pygame
from bin.drawing import Drawing
from bin.map import first_floor
from bin.settings import settings
from bin.player import Player
from bin.sprite_objects import *
from bin.ray_casting import ray_casting
from bin.audio import Audio


class Game:
    def __init__(self, main_menu):
        self.audio = Audio()
        self.main_menu = main_menu
        self.button_bg = pygame.image.load("resources/pics/vignette.png").convert_alpha()

    def run(self):
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        pygame.init()
        screen = pygame.display.set_mode((settings.width, settings.height))
        sprites = Sprites()
        clock = pygame.time.Clock()
        player = Player()
        drawing = Drawing(screen)
        game_music = self.audio.run_music('resources/music/game_music.mp3', settings.volume_music)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_music.stop()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_music.stop()
                        running = False  # Выход из игры

            player.movement()
            screen.fill(settings.black)

            # drawing.background(player.angle)
            pygame.draw.rect(screen, settings.darkred, (0, 0, settings.width, settings.half_height))
            pygame.draw.rect(screen, settings.darkgray, (0, settings.half_height, settings.width, settings.half_height))
            walls = ray_casting(player, drawing.textures)
            drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects])
            drawing.vignette(screen, self.button_bg)
            drawing.fps(clock)

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
        game_music.stop()
        self.main_menu.lobby_music.play(-1)
