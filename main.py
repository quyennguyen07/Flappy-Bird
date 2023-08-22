import pygame
import text
import bird
import tube
import image
import sound

# Flappy bird 2.0
def main():
    def initialize():
        # Initialize tube
        tubes = dict()
        for i in range(1, 3):
            tubes[f'tube{i}'] = tube.Tube(SCREEN_WIDTH, SCREEN_HEIGHT, BLUE)
        # Initialize bird
        bird1 = bird.Bird(30, SCREEN_HEIGHT/2)
        # Initialize text
        txt = text.Text()
        return tubes, bird1, txt

    pygame.mixer.pre_init(frequency= 44100, size= -16, channels= 2, buffer= 512)
    pygame.init()

    # (screen_width + tube_width)/tube_space = num_tube (interger)
    SCREEN_WIDTH, SCREEN_HEIGHT = 350, 550
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Flappy Bird')

    BLUE = (0,0,200)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (200,0,0)

    FLOOR_HEIGHT = 100

    # Initialize image
    bg = image.Image()
    floor1 = image.Image(0, SCREEN_HEIGHT - FLOOR_HEIGHT)
    floor2 = image.Image(0 + SCREEN_WIDTH, SCREEN_HEIGHT - FLOOR_HEIGHT)
    game_over_surface = image.Image(90, 100)
    # Initialize tube, bird, txt
    tubes, bird1, txt = initialize()
    # Initialize sound
    flap_sound = sound.Sound('sound/sfx_wing.wav')
    flap_sound = flap_sound.create_sound()
    hit_sound = sound.Sound('sound/sfx_hit.wav')
    hit_sound = hit_sound.create_sound()
    score_sound = sound.Sound('sound/sfx_point.wav')
    score_sound = score_sound.create_sound()

    # Create image
    bg_img = bg.create_image(SCREEN_WIDTH, SCREEN_HEIGHT, "assets/background-night.png")
    floor1_img = floor1.create_image(SCREEN_WIDTH, FLOOR_HEIGHT, "assets/floor.png")
    floor2_img = floor2.create_image(SCREEN_WIDTH, FLOOR_HEIGHT, "assets/floor.png")
    game_over_surface_img = game_over_surface.create_image(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, "assets/message.png")

    # Initialize variable
    score = 0
    high_score = 0
    font = pygame.font.SysFont('assets/04B_19.TTF', 40)
    run = True
    lost = False
    clock = pygame.time.Clock()

    while run:
        # Chạy n vòng lặp trong 1s
        clock.tick(60)
        lst_img_tubes = []
        
        # Draw background and floor
        bg.draw(screen, bg_img)
        floor1.draw(screen, floor1_img)
        floor2.draw(screen, floor2_img)

        floor1.update_position(floor1_img, SCREEN_WIDTH)
        floor2.update_position(floor2_img, SCREEN_WIDTH)

        # Draw tube
        if not lost:
            for i in tubes:
                tube_img, tube_img_opposite = tubes[i].draw(screen)
                tubes[i].update_tube()
                lst_img_tubes.append(tube_img)
                lst_img_tubes.append(tube_img_opposite)

        # Draw bird
        if not lost:
            bird_img = bird1.draw(screen, bird1.rotate(pygame))
            bird1.flapping()
            bird1.fall(0.25)

        # Blit score
        if not lost:
            text3 = txt.create_text(f'{score}', font, WHITE)
            txt.draw(screen, text3, SCREEN_WIDTH/2, SCREEN_HEIGHT/7)

        # Blit surface finish
        if lost:
            text1 = txt.create_text(f'Score: {score}', font, WHITE)
            txt.draw(screen, text1, SCREEN_WIDTH/2 - text1.get_width()/2, 50)
            text2 = txt.create_text(f'High Score: {high_score}', font, WHITE)
            txt.draw(screen, text2, SCREEN_WIDTH/2 - text2.get_width()/2, SCREEN_HEIGHT - 150 )

            game_over_surface.draw(screen, game_over_surface_img)

        # Calculated score
        for i in tubes:
            if bird1.x > tubes[i].x + tubes[i].TUBE_WIDTH and tubes[i].passed == False:
                score += 1
                tubes[i].passed = True
                score_sound.play()
        if score > high_score:
            high_score = score

        # Handle collision
        for img_tube in lst_img_tubes:
            if bird_img.colliderect(img_tube) or bird1.y > SCREEN_HEIGHT - FLOOR_HEIGHT:
                for i in tubes:
                    tubes[i].tube_vel = 0
                bird1.bird_vel = 0
                lost = True
                hit_sound.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Make bird fly
                    bird1.fly(4)
                    # Flap sound
                    flap_sound.play()
                    # Reset
                    if lost:
                        # ReInitialize
                        tube.Tube.stt = 0
                        score = 0
                        tubes, bird1, txt = initialize()
                        lost = False

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()