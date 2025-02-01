import pygame


class Audio:
    def __init__(self):
        pygame.mixer.init()

    def run_sound(self, filename, volume):
        self.sound = pygame.mixer.Sound(filename)
        self.sound.set_volume(volume)
        return self.sound

    def run_music(self, filename, volume):
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
        return pygame.mixer.music

    def set_music_volume(self, volume):
        return pygame.mixer.music.set_volume(volume)

    def set_sound_volume(self, filename, volume):
        self.sound = pygame.mixer.Sound(filename)
        self.sound.set_volume(volume)
