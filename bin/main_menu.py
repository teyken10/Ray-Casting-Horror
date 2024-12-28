import pygame
import sys
from PIL import Image
from bin.settings import *
from bin.game import Game
from bin.game_properties import Properties
from bin.audio import Audio
from bin.ui.button import Button


class MainMenu:
    def __init__(self, resources):  # Конструктор класса
        self.resources = resources

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("TeXnoPark Lobby")

        # Загрузка GIF и масштабирование его под размеры окна
        self.gif_frames = self.resources.main_menu_frames
        self.num_frames = len(self.gif_frames)

        # Инициализация шрифта
        self.font = pygame.font.Font('resources/main_font.ttf', WIDTH // 40)

        # Загрузка звука
        self.audio = Audio()
        self.hover_sound = self.audio.run("resources/on_button.mp3")
        self.lobby_music = self.audio.run("resources/lobby_music.mp3")

        self.last_hovered_button = None  # Для хранения последней кнопки, на которую наведен курсор

        # Проигрываем фоновую музыку
        self.lobby_music.play(-1)
        print(pygame.RESIZABLE)

    def run(self):
        # Основной цикл
        clock = pygame.time.Clock()

        button = Button(self.screen)

        last_frame_time = pygame.time.get_ticks()  # Время последнего обновления кадра
        frame_duration = 100  # Длительность одного кадра GIF в миллисекундах
        current_frame = 0

        running = True
        while running:
            self.screen.fill(BLACK)
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

            # Отрисовка кнопок
            button_width = int(WIDTH * 0.25)
            button_height = int(HEIGHT * 0.1)

            if button.draw_button("Играть", (WIDTH - button_width) // 2, HEIGHT * 0.3, button_width, button_height,
                                  (0, 0, 0), (255, 0, 0)):
                self.lobby_music.stop()  # Остановка музыки при заходе в игру
                game = Game(self)
                game.run()

            if button.draw_button("Настройки", (WIDTH - button_width) // 2, HEIGHT * 0.45, button_width, button_height,
                                  (0, 0, 0), (255, 0, 0)):
                pygame.mouse.set_pos(0, 0)
                self.screen.fill(BLACK)
                properties = Properties(self.resources)
                properties.run()
                pygame.mouse.set_pos(0, 0)

            if button.draw_button("Выйти", (WIDTH - button_width) // 2, HEIGHT * 0.6, button_width, button_height,
                                  (0, 0, 0), (255, 0, 0)):
                self.lobby_music.stop()  # Остановка музыки при выходе
                pygame.quit()
                sys.exit()

            pygame.display.flip()  # Обновляем экран
            clock.tick(FPS)  # Установка FPS
