import pygame
from bin.audio import Audio
from bin.settings import settings
from bin.game import Game


class Prehistory:
    def __init__(self, main_menu):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.width, settings.height))
        self.audio = Audio()
        self.game = Game(main_menu)
        self.next_page_sound = self.audio.run_sound('resources/sounds/next-page.mp3', settings.volume_sound)
        self.kolokol_sound = self.audio.run_sound('resources/sounds/kolokol.mp3', settings.volume_sound)
        self.first_scene = pygame.image.load("resources/pics/first-scene.png").convert_alpha()
        self.second_scene = pygame.image.load("resources/pics/second-scene.png").convert_alpha()
        self.current_scene = 'first'

    def run(self):
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
                        running = False
                    if event.key == pygame.K_e:
                        if self.current_scene == "first":
                            self.current_scene = "second"  # Переключение на вторую сцену
                            self.next_page_sound.play()
                        else:
                            self.kolokol_sound.play()
                            settings.prehistory = True
                            self.game.run()
                            running = False  # Выход из игры

                    if event.key == pygame.K_q:
                        if self.current_scene == "second":
                            self.current_scene = "first"  # Переключение на вторую сцену
                            self.next_page_sound.play()

            self.screen.fill(settings.black)

            # Отображение текущей сцены
            if self.current_scene == "first":
                scaled_first = pygame.transform.scale(self.first_scene, (settings.width, settings.height))
                self.screen.blit(scaled_first, (0, 0))
            elif self.current_scene == "second":
                scaled_second = pygame.transform.scale(self.second_scene, (settings.width, settings.height))
                self.screen.blit(scaled_second, (0, 0))

            pygame.display.flip()
            clock.tick(settings.fps)

        pygame.mouse.set_visible(True)
        pygame.event.set_grab(False)
