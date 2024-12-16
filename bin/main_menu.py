import pygame
import sys
from PIL import Image
from bin.settings import *
from bin.game import Game

class MainMenu:
    def __init__(self):  # Конструктор класса
        # Инициализация Pygame
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("TeXnoPark Lobby")

        # Загрузка GIF и масштабирование его под размеры окна
        self.gif_frames = self.load_gif('resources/main.gif')
        self.num_frames = len(self.gif_frames)

        # Инициализация шрифта
        self.font = pygame.font.Font('resources/ofont.ru_Unutterable.ttf', WIDTH // 40)

        # Загрузка звука
        pygame.mixer.init()  # Инициализация микшера Pygame
        self.hover_sound = pygame.mixer.Sound("resources/on_button.mp3")
        self.lobby_music = pygame.mixer.Sound("resources/lobby_music.mp3")

        self.last_hovered_button = None  # Для хранения последней кнопки, на которую наведен курсор

        # Проигрываем фоновую музыку
        self.lobby_music.play(-1)  # -1 означает зацикливание, музыка будет играть бесконечно

    def gradient_rect(self, screen, top_color, bottom_color, target_rect):
        colour_rect = pygame.Surface((2, 2))
        pygame.draw.line(colour_rect, top_color, (0, 0), (1, 0))  # Верхняя линия цвета
        pygame.draw.line(colour_rect, bottom_color, (0, 1), (1, 1))  # Нижняя линия цвета
        colour_rect = pygame.transform.smoothscale(colour_rect, (target_rect.width, target_rect.height))  # Растягиваем!
        screen.blit(colour_rect, target_rect)

    # Загрузка анимации из GIF
    def load_gif(self, filename):
        img = Image.open(filename)
        frames = []
        try:
            while True:
                frame = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
                frame = pygame.transform.scale(frame, (WIDTH, HEIGHT))  # Масштабируем кадр под начальное разрешение
                frames.append(frame)
                img.seek(len(frames))
        except EOFError:
            pass
        return frames

    # Функция для рисования кнопки
    def draw_button(self, text, x, y, width, height, color, hover_color):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x <= mouse[0] <= x + width and y <= mouse[1] <= y + height:
            # Если курсор на кнопке, меняем цвет и проверяем
            self.gradient_rect(self.screen, (120, 0, 0), (50, 0, 0), pygame.Rect(x, y, width, height))
            pygame.draw.line(self.screen, (100, 100, 100),
                             (x + WIDTH // 160, y + 10),
                             (x + WIDTH // 160, y + height - 10), WIDTH // 160)

            # Проверяем, чтобы кнопка не являлась последней нажатой кнопкой
            if self.last_hovered_button != text:
                self.hover_sound.play()
                self.last_hovered_button = text

            if click[0] == 1:
                return True
        else:
            self.gradient_rect(self.screen, (0, 0, 15), (15, 0, 0), pygame.Rect(x, y, width, height))
            pygame.draw.line(self.screen, (150, 50, 50),
                             (x + WIDTH // 160, y + 10),
                             (x + WIDTH // 160, y + height - 10), WIDTH // 160)

        label = self.font.render(text, True, (235, 235, 255))

        self.screen.blit(label, (x + (width - label.get_width()) // 2,
                                 y + (height - label.get_height()) // 2))
        return False

    def run(self):
        # Основной цикл
        clock = pygame.time.Clock()

        last_frame_time = pygame.time.get_ticks()  # Время последнего обновления кадра
        frame_duration = 100  # Длительность одного кадра GIF в миллисекундах
        current_frame = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.lobby_music.stop()  # Остановить музыку при выходе
                    pygame.quit()
                    sys.exit()

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

            if self.draw_button("Играть", (WIDTH - button_width) // 2, HEIGHT * 0.3, button_width, button_height,
                                (0, 0, 0), (255, 0, 0)):
                self.lobby_music.stop()  # Остановка музыки при заходе в игру
                game = Game()
                game.run()

            if self.draw_button("Настройки", (WIDTH - button_width) // 2, HEIGHT * 0.45, button_width, button_height,
                                (0, 0, 0), (255, 0, 0)):
                print("Настройки нажата")

            if self.draw_button("Выйти", (WIDTH - button_width) // 2, HEIGHT * 0.6, button_width, button_height,
                                (0, 0, 0), (255, 0, 0)):
                self.lobby_music.stop()  # Остановка музыки при выходе
                pygame.quit()
                sys.exit()

            pygame.display.flip()  # Обновляем экран
            clock.tick(60)  # Установка FPS
