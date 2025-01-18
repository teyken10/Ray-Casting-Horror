import pygame


class Audio:
    def __init__(self):
        pygame.mixer.init()

    def run_sound(self, filename, volume):
        sound = pygame.mixer.Sound(filename)
        sound.set_volume(volume)
        return sound

    def run_music(self, filename, volume):
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
        return pygame.mixer.music

    def set_volume(self, volume):
        return pygame.mixer.music.set_volume(volume)

    def get_volume(self):
        return pygame.mixer.music.get_volume()
