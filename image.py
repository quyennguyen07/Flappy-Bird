import pygame

class Image:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def create_image(self, width, height, directory):
        return pygame.transform.scale(pygame.image.load(directory), (width, height))
        
    def draw(self, screen, img):
        screen.blit(img, (self.x, self.y))

    def update_position(self, img, scr_wid):
        img_width = img.get_width()
        self.x -= 1
        if self.x + img_width == 0:
            self.x = scr_wid


