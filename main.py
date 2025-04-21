import pygame
import sys
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        updatable.update(dt)
        scr.fill(BLACK)
        for obj in drawable:
            obj.draw(scr)
        
        for asteroid in asteroids:
            collision = asteroid.check_collision(player)
            
            if collision:
                print("Game Over!")
                return
            
            for shot in shots:
                hit = shot.check_collision(asteroid)
                if hit:
                    shot.kill()
                    asteroid.split()


        pygame.display.flip()

        ms_passed = clock.tick(FPS)
        dt = ms_passed / 1000





if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()