import pygame
from bin.settings import *
from bin.audio import Audio

class Button:
    def __init__(self, screen):
        # Загрузка звука
        pygame.mixer.init()
        self.audio = Audio()
        self.hover_sound = self.audio.run("resources/on_button.mp3")

        # Инициализация шрифта
        self.font = pygame.font.Font('resources/main_font.ttf', WIDTH // 40)

        self.screen = screen
        self.last_hovered_button = None  # Для хранения последней кнопки, на которую наведен курсор

    def gradient_rect(self, screen, top_color, bottom_color, target_rect):
        colour_rect = pygame.Surface((2, 2))
        pygame.draw.line(colour_rect, top_color, (0, 0), (1, 0))  # Верхняя линия цвета
        pygame.draw.line(colour_rect, bottom_color, (0, 1), (1, 1))  # Нижняя линия цвета
        colour_rect = pygame.transform.smoothscale(colour_rect, (target_rect.width, target_rect.height))  # Растягиваем!
        screen.blit(colour_rect, target_rect)

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
