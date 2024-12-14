import pygame
import sys
from PIL import Image
from bin.settings import *
from bin.game import Game


class MainMenu:
    def __init__(self):
        # Инициализация Pygame
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("TeXnoPark Lobby")

        # Загрузка GIF
        self.gif_frames = self.load_gif('resources/main.gif')
        self.num_frames = len(self.gif_frames)

        # Инициализация шрифта
        self.font = pygame.font.SysFont('Arial', 40)

    # Загрузка анимации из GIF
    def load_gif(self, filename):
        img = Image.open(filename)
        frames = []
        try:
            while True:
                frame = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
                frame = pygame.transform.scale(frame, (WIDTH, HEIGHT))
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
            pygame.draw.rect(self.screen, hover_color, (x, y, width, height))
            if click[0] == 1:
                return True
        else:
            pygame.draw.rect(self.screen, color, (x, y, width, height))

        label = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(label, (x + (width - label.get_width()) // 2, y + (height - label.get_height()) // 2))
        return False

    def run(self):
        # Основной цикл
        clock = pygame.time.Clock()
        frame_time = 1000 // FPS  # Время на каждый кадр в миллисекундах
        last_frame_time = pygame.time.get_ticks()  # Время последнего обновления кадра
        frame_duration = 100  # Длительность одного кадра GIF в миллисекундах
        current_frame = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # if event.type == pygame.VIDEORESIZE:
                #     W, H = event.w, event.h
                #     screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

            # Отображение текущего кадра GIF
            self.screen.blit(self.gif_frames[current_frame], (0, 0))

            # Обновление текущего кадра с оптимизацией под FPS
            current_time = pygame.time.get_ticks()
            if current_time - last_frame_time >= frame_duration:  # Проверяем, прошло ли достаточно времени
                current_frame = (current_frame + 1) % self.num_frames  # Переход к следующему кадру
                last_frame_time = current_time  # Обновляем время последнего кадра

            # Отрисовка кнопок относительно размеров экрана
            button_width = int(WIDTH * 0.25)
            button_height = int(HEIGHT * 0.1)

            if self.draw_button("Играть", (WIDTH - button_width) // 2, HEIGHT * 0.3, button_width, button_height,
                           (0, 0, 0), (255, 0, 0)):
                game = Game()
                game.run()

            if self.draw_button("Настройки", (WIDTH - button_width) // 2, HEIGHT * 0.45, button_width, button_height,
                           (0, 0, 0), (255, 0, 0)):
                print("Настройки нажата")

            if self.draw_button("Выйти", (WIDTH - button_width) // 2, HEIGHT * 0.6, button_width, button_height,
                           (0, 0, 0), (255, 0, 0)):
                pygame.quit()
                sys.exit()

            pygame.display.flip()  # Обновляем экран
            clock.tick(FPS)  # Установка FPS
