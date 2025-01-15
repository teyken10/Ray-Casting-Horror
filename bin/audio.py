import pygame


class Audio:
    def __init__(self):
        pygame.mixer.init()

    def run(self, filename):
        return pygame.mixer.Sound(filename)

    def set_volume(self, volume):
        return pygame.mixer.music.set_volume(volume)

    def get_volume(self):
        return pygame.mixer.music.get_volume()
