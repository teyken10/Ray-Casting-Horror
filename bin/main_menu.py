import pygame
import sys
from bin.settings import settings
from bin.prehistory import Prehistory
from bin.game_properties import Properties
from bin.game import Game
from bin.audio import Audio
from bin.ui.button import Button


class MainMenu:
    def __init__(self, resources):  # Конструктор класса
        self.resources = resources

        self.screen = pygame.display.set_mode((settings.width, settings.height), pygame.RESIZABLE)
        pygame.display.set_caption("TeXnoPark Lobby")

        # Загрузка GIF и масштабирование его под размеры окна
        self.gif_frames = self.resources.main_menu_frames
        self.num_frames = len(self.gif_frames)

        # Инициализация шрифта
        self.font = pygame.font.Font('resources/fonts/main_font.ttf', settings.width // 40)

        # Загрузка звука
        self.audio = Audio()
        self.hover_sound = self.audio.run_sound("resources/sounds/on_button.mp3", settings.volume_sound)
        self.lobby_music = self.audio.run_music("resources/music/lobby_music.mp3", settings.volume_music)

        self.last_hovered_button = None  # Для хранения последней кнопки, на которую наведен курсор

    def draw_rect_alpha(self, screen, color, rect):
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
        screen.blit(shape_surf, rect)

    def run(self):
        # Основной цикл
        clock = pygame.time.Clock()

        button = Button(self.screen)

        last_frame_time = pygame.time.get_ticks()  # Время последнего обновления кадра
        frame_duration = 100  # Длительность одного кадра GIF в миллисекундах
        current_frame = 0

        running = True
        while running:
            self.screen.fill(settings.black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.lobby_music.stop()  # Остановить музыку при выходе
                    exit()

            # Отображение текущего кадра GIF
            scaled_frame = self.gif_frames[current_frame]
            self.screen.blit(scaled_frame, (0, 0))

            # Обновление текущего кадра с оптимизацией под FPS
            current_time = pygame.time.get_ticks()
            if current_time - last_frame_time >= frame_duration:  # Проверяем, прошло ли достаточно времени
                current_frame = (current_frame + 1) % self.num_frames  # Переход к следующему кадру
                last_frame_time = current_time  # Обновляем время последнего кадра

            self.draw_rect_alpha(self.screen, (0, 0, 0, 150), (0, 0, settings.width, settings.height))

            # Отрисовка кнопок
            button_width = int(settings.width * 0.25)
            button_height = int(settings.height * 0.1)

            if button.draw_button("Играть", (settings.width - button_width) // 2, settings.height * 0.3, button_width,
                                  button_height):
                self.lobby_music.stop()  # Остановка музыки при заходе в игру
                if settings.prehistory:
                    game = Game(self)
                    game.run()
                else:
                    preh = Prehistory(self)
                    preh.run()

            if button.draw_button("Настройки", (settings.width - button_width) // 2, settings.height * 0.45,
                                  button_width, button_height):
                # pygame.mouse.set_pos(0, 0)
                self.screen.fill(settings.black)
                properties = Properties(self.resources)
                properties.run()
                # pygame.mouse.set_pos(0, 0)

            if button.draw_button("Выйти", (settings.width - button_width) // 2, settings.height * 0.6, button_width,
                                  button_height):
                self.lobby_music.stop()  # Остановка музыки при выходе
                pygame.quit()
                sys.exit()

            pygame.display.flip()  # Обновляем экран
            clock.tick(settings.fps)  # Установка FPS
