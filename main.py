import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    pygame.init()

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    scr_width = SCREEN_WIDTH
    scr_height = SCREEN_HEIGHT
    scr = pygame.display.set_mode((scr_width, scr_height))
    pygame.display.set_caption("Asteroids")
    
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        scr.fill(BLACK)
        player.draw(scr)
        pygame.display.flip()

        ms_passed = clock.tick(FPS)
        dt = ms_passed / 1000





if __name__ == "__main__":
    main()