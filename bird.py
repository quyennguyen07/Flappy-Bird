import pygame

class Bird:
    bird_vel = 0
    BIRD_WIDTH = 40
    BIRD_HEIGHT = 40

    # Load image bird
    bird_img_up = pygame.transform.scale(pygame.image.load('assets/yellowbird-upflap.png'), (BIRD_WIDTH, BIRD_HEIGHT))
    bird_img_mid = pygame.transform.scale(pygame.image.load('assets/yellowbird-midflap.png'), (BIRD_WIDTH, BIRD_HEIGHT))
    bird_img_down = pygame.transform.scale(pygame.image.load('assets/yellowbird-downflap.png'), (BIRD_WIDTH, BIRD_HEIGHT))
    bird_lst = [bird_img_up, bird_img_mid, bird_img_down]
    bird_lst_index = 0
    bird_img = bird_lst[bird_lst_index]


    def __init__(self, bird_x, bird_y):
        self.x = bird_x
        self.y = bird_y

    # draw bird
    def draw(self, screen, bird_rotate):
        return screen.blit(bird_rotate, (self.x, self.y))
    
    # Make bird fall
    def fall(self, GRAVITY):
        self.y += self.bird_vel
        self.bird_vel += GRAVITY
    
    # Make bird flapping
    def flapping(self):
        if self.bird_vel < 0:
            self.bird_img = self.bird_lst[0]
        elif self.bird_vel == 0:
            self.bird_img = self.bird_lst[1]
        elif self.bird_vel > 0:
            self.bird_img = self.bird_lst[2]

    # Make bird roto
    def rotate(self, pygame):
        return pygame.transform.rotozoom(self.bird_img, -self.bird_vel * 4, 1)

    # Make bird fly
    def fly(self, m):
        self.bird_vel = 0
        self.bird_vel -= m
