import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from bullet import Bullet

drawable = pygame.sprite.Group()
updateable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
bullets = pygame.sprite.Group()
remove_if_out_of_bounds = pygame.sprite.Group()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    py_clock = pygame.time.Clock()

    Player.containers = (drawable, updateable)
    Asteroid.containers = (asteroids, drawable, updateable, remove_if_out_of_bounds)
    AsteroidField.containers = (updateable)
    Bullet.containers = (bullets, drawable, updateable, remove_if_out_of_bounds)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.quit:
                return

        screen.fill((0, 0, 0))
        
        for draw_object in drawable:
            draw_object.draw(screen)

        for asteroid in asteroids:
            for bullet in bullets:
                if asteroid.collision(bullet):
                    asteroid.take_hit()
                    bullet.kill()
            if asteroid.collision(player):
                print("GAME OVER")
                sys.exit()

        for entity in remove_if_out_of_bounds:
            entity.remove_out_of_bounds(dt)

        updateable.update(dt)

        pygame.display.flip()
        dt = py_clock.tick(FRAMERATE)/1000

if __name__ == "__main__":
    main()
