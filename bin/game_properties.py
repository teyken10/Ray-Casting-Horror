import pygame
from PIL import Image
from bin.settings import *
from bin.ui.button import Button
from bin.audio import Audio


class Properties:
    def __init__(self, resources):  # Конструктор класса
        self.resources = resources
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("TeXnoPark Settings")

        self.audio = Audio()
        self.audio.set_volume(0.5)

        self.gif_frames = self.resources.main_menu_frames
        self.num_frames = len(self.gif_frames)

        # Инициализация шрифта
        self.font = pygame.font.Font('resources/main_font.ttf', WIDTH // 40)

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
        clock = pygame.time.Clock()

        button = Button(self.screen)

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
            self.screen.blit(scaled_frame, (0, 0))

            # Обновление текущего кадра с оптимизацией под FPS
            current_time = pygame.time.get_ticks()
            if current_time - last_frame_time >= frame_duration:  # Проверяем, прошло ли достаточно времени
                current_frame = (current_frame + 1) % self.num_frames  # Переход к следующему кадру
                last_frame_time = current_time  # Обновляем время последнего кадра

            # Отрисовка кнопок
            button_width = int(WIDTH * 0.25)
            button_height = int(HEIGHT * 0.1)

            # Проверяем и отрисовываем кнопки
            if button.draw_button("Вернуться", (WIDTH - button_width) // 2, HEIGHT * 0.7,
                                  button_width, button_height):
                running = False

            if button.draw_button("+", (WIDTH - button_width) // 2, HEIGHT * 0.45,
                                  button_width * 0.3, button_height):
                self.audio.set_volume(min(self.audio.get_volume() + 0.1, 1.0))  # Ограничиваем до 1.0

            if button.draw_button("-", (WIDTH - button_width) // 2 * 1.47, HEIGHT * 0.45,
                                  button_width * 0.3, button_height):
                self.audio.set_volume(max(self.audio.get_volume() - 0.1, 0.0))  # Ограничиваем до 0.0

            text = self.font.render(f'{int(self.audio.get_volume() * 100)}', True, (100, 255, 100))
            text_x = WIDTH // 2 - text.get_width() // 2
            text_y = HEIGHT // 2 - text.get_height() // 2
            self.screen.blit(text, (text_x, text_y))

            pygame.display.flip()  # Обновляем экран
            clock.tick(FPS)  # Установка FPS
