import pygame
from bin.audio import Audio
from bin.settings import settings
from math import degrees


class End:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.width, settings.height))
        self.main_im = pygame.image.load("resources/pics/end-game.png").convert_alpha()
        pygame.display.set_caption("The End (Esc - exit)")
        self.font = pygame.font.Font('resources/fonts/main_font.ttf', settings.width // 30)

    def run(self):
        with open('resources/data/time.txt', 'r', encoding='utf-8') as f:
            time_in_game = int(f.read())
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()

            self.screen.fill(settings.black)

            scaled_im = pygame.transform.scale(self.main_im, (settings.width, settings.height))
            self.screen.blit(scaled_im, (0, 0))
            text_time = self.font.render(f'Время прохождения игры: {time_in_game} секунд', True, settings.white)
            self.screen.blit(text_time, (185, 50))

            pygame.display.flip()
            clock.tick(settings.fps)

        pygame.mouse.set_visible(True)
        pygame.event.set_grab(False)
