import pygame

class Sound:
    def __init__(self, directory):
        self.directory = directory

    def create_sound(self):
        return pygame.mixer.Sound(self.directory)