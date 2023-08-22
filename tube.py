from random import randrange
import pygame

class Tube:
    passed = False
    TUBE_WIDTH = 50
    TUBE_SPACE = 200
    TUBE_GAP = 150
    tube_vel = 3
    stt  = 0

    FLOOR_HEIGHT = 100

    # Load image tube
    tube_img = pygame.image.load('assets/pipe-green.png')

    def __init__(self, screen_wid, screen_hei, color):
        self.screen_wid = screen_wid
        self.screen_hei = screen_hei

        self.x = self.screen_wid + Tube.TUBE_SPACE * Tube.stt
        self.y = 0
        self.color = color
        self.tube_height = randrange(0, self.screen_hei - Tube.FLOOR_HEIGHT - Tube.TUBE_GAP)

        self.y_opposite = self.tube_height + Tube.TUBE_GAP
        self.tube_height_opposite = (self.screen_hei - Tube.FLOOR_HEIGHT) - (self.tube_height + Tube.TUBE_GAP)

        self.tube_img = pygame.transform.scale(Tube.tube_img, (Tube.TUBE_WIDTH, self.tube_height))
        self.tube_img = pygame.transform.flip(self.tube_img, False, True) # flip image
        self.tube_img_opposite = pygame.transform.scale(Tube.tube_img, (Tube.TUBE_WIDTH, self.tube_height_opposite))

        Tube.stt += 1

    # Draw tube
    def draw(self, screen):
        tube = screen.blit(self.tube_img, (self.x, self.y))
        tube_opposite = screen.blit(self.tube_img_opposite, (self.x, self.y_opposite))
        return tube, tube_opposite

    # Update tube
    def update_tube(self):
        self.x -= self.tube_vel
        if self.x + self.TUBE_WIDTH < 0:
            self.x = self.screen_wid

            self.tube_height = randrange(0, self.screen_hei - Tube.FLOOR_HEIGHT - Tube.TUBE_GAP)
            self.y_opposite = self.tube_height + Tube.TUBE_GAP
            self.tube_height_opposite = (self.screen_hei - Tube.FLOOR_HEIGHT) - (self.tube_height + Tube.TUBE_GAP)

            self.tube_img = pygame.transform.scale(Tube.tube_img, (Tube.TUBE_WIDTH, self.tube_height))
            self.tube_img = pygame.transform.flip(self.tube_img, False, True) # flip image
            self.tube_img_opposite = pygame.transform.scale(Tube.tube_img, (Tube.TUBE_WIDTH, self.tube_height_opposite))

            self.passed = False