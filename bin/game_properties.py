import pygame
from PIL import Image
from bin.settings import *
from bin.ui.button import Button
from bin.audio import Audio


class Properties:
    def __init__(self, resources):  # Конструктор класса, исправлено на init
        self.resources = resources
        self.screen = pygame.display.set_mode((settings.width, settings.height), pygame.RESIZABLE)
        pygame.display.set_caption("TeXnoPark Settings")

        self.audio = Audio()
        self.audio.set_music_volume(settings.volume_music)

        self.gif_frames = self.resources.main_menu_frames
        self.num_frames = len(self.gif_frames)

        # Инициализация шрифта
        self.font = pygame.font.Font('resources/main_font.ttf', settings.width // 40)

    def load_gif(self, filename):
        img = Image.open(filename)
        frames = []
        try:
            while True:
                frame = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
                frame = pygame.transform.scale(frame, (
                    settings.width, settings.height))  # Масштабируем кадр под начальное разрешение
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

            # Отрисовка кнопок для громкости музыки
            button_width = int(settings.width * 0.25)
            button_height = int(settings.height * 0.1)

            music_volume_text = self.font.render("Громкость музыки", True, settings.sandy)
            self.screen.blit(music_volume_text, (10, 10))

            if button.draw_button("+", 10, 50, button_width * 0.3, button_height):
                if settings.volume_music < 100:
                    settings.volume_music += 1
                    self.audio.set_music_volume(settings.volume_music / 100)

            if button.draw_button("-", 10 + button_width * 0.3 + 10, 50, button_width * 0.3, button_height):
                if settings.volume_music > 0:
                    settings.volume_music -= 1
                    self.audio.set_music_volume(settings.volume_music / 100)

            music_volume_display = self.font.render(f'{settings.volume_music}', True, settings.pink)
            self.screen.blit(music_volume_display, (10 + button_width * 0.6 + 15, 60))

            # Отрисовка кнопок для громкости звуков
            sound_volume_text = self.font.render("Громкость звуков", True, settings.sandy)
            self.screen.blit(sound_volume_text, (10, 200))

            if button.draw_button("+", 10, 240, button_width * 0.3, button_height):
                if settings.volume_sound < 100:
                    settings.volume_sound += 1
                    # Обновляем громкость звука
                    button.update_sound_volume(settings.volume_sound / 100)

            if button.draw_button("-", 10 + button_width * 0.3 + 10, 240, button_width * 0.3, button_height):
                if settings.volume_sound > 0:
                    settings.volume_sound -= 1
                    # Обновляем громкость звука
                    button.update_sound_volume(settings.volume_sound / 100)

            sound_volume_display = self.font.render(f'{settings.volume_sound}', True, settings.pink)
            self.screen.blit(sound_volume_display, (10 + button_width * 0.6 + 15, 250))

            # Отрисовка настройки чувствительности
            sensitivity_text = self.font.render("Чувствительность", True, settings.sandy)
            self.screen.blit(sensitivity_text, (settings.width - settings.height // 2.28, 10))

            if button.draw_button("+", settings.width - settings.height // 2.28, 50, button_width * 0.3, button_height):
                if settings.sensitivity < 100:
                    settings.sensitivity += 0.0001  # Увеличиваем чувствительность

            if button.draw_button("-", settings.width - settings.height // 2.28 + button_width * 0.3 + 10, 50, button_width * 0.3,
                                  button_height):
                if settings.sensitivity > 0.0001:
                    settings.sensitivity -= 0.0001  # Уменьшаем чувствительность

            sensitivity_display = self.font.render(f'{settings.sensitivity}', True, settings.pink)
            self.screen.blit(sensitivity_display, (settings.width - settings.height // 2.28 + button_width * 0.6 + 15, 60))

            # Настройки размера экрана
            screen_size_text = self.font.render("Размер экрана", True, settings.sandy)
            self.screen.blit(screen_size_text, (settings.width // 2 - 130, 10))

            screen_sizes = ["2560x1440", "1920x1080", "1200x800"]  # Предложенные варианты
            for i, size in enumerate(screen_sizes):
                if button.draw_button(size, settings.width // 2 - settings.width // 8.5, 40 + i * 80, button_width, button_height):
                    if size == "2560x1440":
                        settings.width, settings.height = 2560, 1440
                    if size == "1920x1080":
                        settings.width, settings.height = 1920, 1080
                    if size == "1200x800":
                        settings.width, settings.height = 1200, 800
                    running = False

            # Настройка переключения между мониторами
            monitor_text = self.font.render("Выбрать монитор", True, settings.sandy)
            self.screen.blit(monitor_text, (settings.width // 2 - 145, 350))

            monitors = ["Монитор 1", "Монитор 2"]
            for i, monitor in enumerate(monitors):
                if button.draw_button(monitor, settings.width // 2 - settings.width // 8.5, 450 + i * 80, button_width, button_height):
                    if monitor == "Монитор 1":
                        print("Монитор 1")
                    if monitor == "Монитор 2":
                        print("Монитор 2")


            # Кнопка "Вернуться"
            if button.draw_button("Вернуться", (settings.width - button_width) // 2, settings.height * 0.85,
                                  button_width, button_height):
                running = False

            pygame.display.flip()  # обновляем экран
            clock.tick(settings.fps)  # установка fps
