import pygame
from PIL import Image
from bin.settings import *
from bin.ui.button import Button


class Properties:
    def __init__(self):  # Конструктор класса
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("TeXnoPark Settings")

        self.gif_frames = self.load_gif('resources/main.gif')
        self.num_frames = len(self.gif_frames)

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

    def run(self):
        # Основной цикл
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()

        button = Button(screen)

        last_frame_time = pygame.time.get_ticks()  # Время последнего обновления кадра
        frame_duration = 100  # Длительность одного кадра GIF в миллисекундах
        current_frame = 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            # Отображение текущего кадра GIF
            scaled_frame = self.gif_frames[current_frame]
            screen.blit(scaled_frame, (0, 0))

            # Обновление текущего кадра с оптимизацией под FPS
            current_time = pygame.time.get_ticks()
            if current_time - last_frame_time >= frame_duration:  # Проверяем, прошло ли достаточно времени
                current_frame = (current_frame + 1) % self.num_frames  # Переход к следующему кадру
                last_frame_time = current_time  # Обновляем время последнего кадра

            # Отрисовка кнопок
            button_width = int(WIDTH * 0.25)
            button_height = int(HEIGHT * 0.1)

            if button.draw_button("Вернуться", (WIDTH - button_width) // 2, HEIGHT * 0.45, button_width, button_height,
                                  (0, 0, 0), (255, 0, 0)):
                running = False

            pygame.display.flip()  # Обновляем экран
            clock.tick(FPS)  # Установка FPS
