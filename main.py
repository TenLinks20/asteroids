import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    pygame.init()

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    scr_width = SCREEN_WIDTH
    scr_height = SCREEN_HEIGHT
    scr = pygame.display.set_mode((scr_width, scr_height))
    pygame.display.set_caption("Asteroids")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        scr.fill(BLACK)
        pygame.display.flip()





if __name__ == "__main__":
    main()