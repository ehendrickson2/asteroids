import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    # Initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers
    Player.containers = (updatable, drawable)

    Shot.containers = (updatable, drawable, shots)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    # Instantiate objects after assigning to groups/containers
    player = Player(x, y)
    AsteroidField()

    # Start Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Set black background
        screen.fill((0, 0, 0))

        updatable.update(dt)

        for asteroid in asteroids:
            if Asteroid.collision(asteroid, player):
                print("Game over!")
                return

        for thing in drawable:
            thing.draw(screen)

        clock.tick(60)
        dt = clock.get_time() / 1000
        pygame.display.flip()


if __name__ == "__main__":
    main()
