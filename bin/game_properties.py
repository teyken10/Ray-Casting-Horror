import pygame
from PIL import Image
from bin.settings import *
from bin.ui.button import Button
from bin.audio import Audio


class Properties:
    def __init__(self, resources):
        self.resources = resources
        self.screen = pygame.display.set_mode((settings.width, settings.height), pygame.RESIZABLE)
        pygame.display.set_caption("TeXnoPark Settings")

        self.gif_frames = self.resources.game_properties_frames
        self.num_frames = len(self.gif_frames)

        self.audio = Audio()
        self.audio.set_music_volume(settings.volume_music)

        # Инициализация шрифта
        self.font = pygame.font.Font('resources/fonts/main_font.ttf', settings.width // 40)
        self.font_head = pygame.font.Font('resources/fonts/main_font.ttf', settings.width // 10)

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

            self.draw_rect_alpha(self.screen, (0, 0, 0, 100), (0, 0, settings.width, settings.height))

            # Отрисовка кнопок для громкости музыки
            button_width = int(settings.width * 0.25)
            button_height = int(settings.height * 0.1)

            headline_text = self.font_head.render('НАСТРОЙКИ', True, settings.red)
            self.screen.blit(headline_text, (settings.width // 6, 50))

            music_volume_text = self.font.render("Громкость музыки", True, settings.sandy)
            self.screen.blit(music_volume_text, (10, 250))

            if button.draw_button("+", 10, 300, button_width * 0.3, button_height):
                if settings.volume_music < 1:
                    settings.volume_music += 0.01
                    self.audio.set_music_volume(settings.volume_music)

            if button.draw_button("-", 10 + button_width * 0.3 + 10, 300, button_width * 0.3, button_height):
                if settings.volume_music > 0:
                    settings.volume_music -= 0.01
                    self.audio.set_music_volume(settings.volume_music)

            music_volume_display = self.font.render(f'{int(settings.volume_music * 100)}', True, settings.pink)
            self.screen.blit(music_volume_display, (10 + button_width * 0.6 + 15, 310))

            # Отрисовка кнопок для громкости звуков
            sound_volume_text = self.font.render("Громкость звуков", True, settings.sandy)
            self.screen.blit(sound_volume_text, (10, 450))

            if button.draw_button("+", 10, 500, button_width * 0.3, button_height):
                if settings.volume_sound < 1:
                    settings.volume_sound += 0.01
                    # Обновляем громкость звука
                    button.update_sound_volume(settings.volume_sound)

            if button.draw_button("-", 10 + button_width * 0.3 + 10, 500, button_width * 0.3, button_height):
                if settings.volume_sound > 0:
                    settings.volume_sound -= 0.01
                    # Обновляем громкость звука
                    button.update_sound_volume(settings.volume_sound)

            sound_volume_display = self.font.render(f'{int(settings.volume_sound * 100)}', True, settings.pink)
            self.screen.blit(sound_volume_display, (10 + button_width * 0.6 + 15, 510))

            # Отрисовка настройки чувствительности
            sensitivity_text = self.font.render("Чувствительность", True, settings.sandy)
            self.screen.blit(sensitivity_text, (settings.width - settings.height // 2.28, 250))

            if button.draw_button("+", settings.width - settings.height // 2.28, 300, button_width * 0.3, button_height):
                if settings.sensitivity < 100:
                    settings.sensitivity += 0.0001  # Увеличиваем чувствительность

            if button.draw_button("-", settings.width - settings.height // 2.28 + button_width * 0.3 + 10, 300,
                                  button_width * 0.3,
                                  button_height):
                if settings.sensitivity > 0.0001:
                    settings.sensitivity -= 0.0001  # Уменьшаем чувствительность

            sensitivity_display = self.font.render(f'{settings.sensitivity}', True, settings.pink)
            self.screen.blit(sensitivity_display,
                             (settings.width - settings.height // 2.28 + button_width * 0.6 + 15, 310))

            # Настройки размера экрана
            # pygame.draw.rect(self.screen, settings.black, (settings.width // 2 - 130, 250, 100, 100), 10)
            screen_size_text = self.font.render("Количество FPS", True, settings.sandy)
            self.screen.blit(screen_size_text, (settings.width // 2 - 130, 250))

            screen_sizes = ["30", "60", "120", '165']  # Предложенные варианты
            for i, fps in enumerate(screen_sizes):
                if button.draw_button(fps, settings.width // 2 - settings.width // 8.5 + 80,
                                      300 + i * 60, button_width // 2, button_height // 1.5):
                    if fps == "30":
                        settings.fps = 30
                        settings.player_speed = 165 / settings.fps
                    if fps == "60":
                        settings.fps = 60
                        settings.player_speed = 165 / settings.fps
                    if fps == "120":
                        settings.fps = 120
                        settings.player_speed = 165 / settings.fps
                    if fps == "165":
                        settings.fps = 165
                        settings.player_speed = 165 / settings.fps

            # Кнопка "Вернуться"
            if button.draw_button("Вернуться", (settings.width - button_width) // 2, settings.height * 0.85,
                                  button_width, button_height):
                running = False

            pygame.display.flip()  # обновляем экран
            clock.tick(settings.fps)  # установка fps
