import pygame
from PIL import Image
from bin.settings import *


class ResourceManager:
    def __init__(self):
        self.main_menu_frames = self.load_gif('resources/main.gif')

    # Загрузка анимации из GIF
    def load_gif(self, filename):
        img = Image.open(filename)
        frames = []
        try:
            while True:
                frame = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
                frame = pygame.transform.scale(frame, (settings.width, settings.height))
                frames.append(frame)
                img.seek(len(frames))
        except EOFError:
            pass
        return frames
