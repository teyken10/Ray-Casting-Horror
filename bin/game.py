import pygame
from bin.settings import *
from bin.player import Player
from bin.ray_casting import ray_casting
from bin.audio import Audio


class Game:
    def __init__(self):
        self.audio = Audio()
        self.lobby_music = self.audio.run("resources/lobby_music.mp3")

    def run(self):
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()
        player = Player()

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
                    print(event)
                    print(event.pos)

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
        from bin.main_menu import MainMenu  # Импортируем здесь, чтобы избежать кругового импорта
        main_menu = MainMenu()  # Создаем экземпляр MainMenu
        main_menu.lobby_music.play(-1)  # Запускаем фоновую музыку
        main_menu.run()  # Запускаем главное меню
