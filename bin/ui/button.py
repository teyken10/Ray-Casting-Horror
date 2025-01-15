import pygame
from bin.settings import *
from bin.audio import Audio


class Button:
    def __init__(self, screen):
        # Загрузка звука
        pygame.mixer.init()
        self.audio = Audio()
        self.hover_sound = self.audio.run("resources/on_button.mp3")

        # Загружаем изображение фона кнопки
        self.button_bg = pygame.image.load("resources/blood_button.png").convert_alpha()

        # Инициализация шрифта
        self.font = pygame.font.Font('resources/main_font.ttf', WIDTH // 40)

        self.screen = screen
        self.last_hovered_button = None  # Для хранения последней кнопки, на которую наведен курсор

    def draw_button(self, text, x, y, width, height):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]  # Левый клик мыши

        # Проверяем, наведён ли курсор на кнопку
        if x <= mouse[0] <= x + width and y <= mouse[1] <= y + height:
            # Если курсор на кнопке, отображаем растянутое изображение
            scaled_bg = pygame.transform.scale(self.button_bg, (width, height))
            self.screen.blit(scaled_bg, (x, y))
            # Проигрываем звук при наведении
            if self.last_hovered_button != text:
                self.hover_sound.play()
                self.last_hovered_button = text

            if click:
                return True

        # Отображаем текст кнопки
        label = self.font.render(text, True, (235, 235, 255))
        self.screen.blit(label, (x + (width - label.get_width()) // 2,
                                 y + (height - label.get_height()) // 2))
        return False
