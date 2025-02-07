import pygame
from bin.settings import *
from bin.audio import Audio


class Button:
    def __init__(self, screen):  # Исправлено с init на __init__
        # Загрузка звука
        pygame.mixer.init()
        self.audio = Audio()
        self.hover_sound = self.audio.run_sound("resources/sounds/on_button.mp3", settings.volume_sound)

        # Загружаем изображение фона кнопки
        self.button_bg = pygame.image.load("resources/pics/blood_button.png").convert_alpha()

        # Инициализация шрифта
        self.font = pygame.font.Font('resources/fonts/main_font.ttf', settings.width // 40)

        self.screen = screen
        self.last_hovered_button = None  # Для хранения последней кнопки, на которую наведен курсор

        self.time_motion = settings.fps // 5
        self.time = 0

    def update_sound_volume(self, volume):
        self.hover_sound.set_volume(volume)

    def draw_button(self, text, x, y, width, height):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]  # Левый клик мыши
        if not click:
            self.time = 0
            self.time_motion = settings.fps // 3

        scaled_bg = pygame.transform.scale(self.button_bg, (width, height))
        # Проверяем, наведён ли курсор на кнопку
        if x <= mouse[0] <= x + width and y <= mouse[1] <= y + height:
            # Если курсор на кнопке, отображаем растянутое изображение
            self.screen.blit(scaled_bg, (x, y))
            # Проигрываем звук при наведении
            if self.last_hovered_button != text:
                self.hover_sound.play()
                self.last_hovered_button = text

            if click:
                if self.time == 0:
                    self.time += 6
                    return True
                elif self.time_motion <= self.time:
                    self.time_motion = settings.fps // 12
                    self.time = 0
                else:
                    self.time += 1

        # Отображаем текст кнопки
        label = self.font.render(text, True, (235, 235, 255))
        self.screen.blit(label, (x + (width - label.get_width()) // 2,
                                 y + (height - label.get_height()) // 2))
        return False
