import pygame


class Audio:
    def __init__(self):
        pass

    def run(self, filename):
        return pygame.mixer.Sound(filename)
