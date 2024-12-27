import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField

def main():
    pygame.init()
    frameclock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = updateable

    asteroid_field = AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for updateable_item in updateable:
            updateable_item.update(dt)

        screen.fill((0,0,0))
             

        for drawable_item in drawable:
            drawable_item.draw(screen)

        pygame.display.flip()
        dt = frameclock.tick(60) / 1000

if __name__ == "__main__":
    main()