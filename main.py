import pygame
import os
from constants import *
from tools import Tools
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    # Initialization
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Screen setup
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_rect = screen.get_rect()

    # Background image
    image = pygame.transform.scale(
        pygame.image.load(os.path.join(BASE_PATH, "background.jpeg")).convert(),
        (SCREEN_WIDTH, SCREEN_HEIGHT),
    )
    image.set_alpha(100)

    # Setup tools and score display
    tools = Tools(screen)
    tools.font_init(screen.get_rect())

    pygame.display.set_caption("Asteroids")

    # Set clock and deltatime(dt)
    clock = pygame.time.Clock()
    dt = 0

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

    # Player position
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

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
        screen.blit(image, (0, 0))

        updatable.update(dt)

        for asteroid in asteroids:
            if Asteroid.collision(asteroid, player):
                print("Game over!")
                print(f"Your score was {player.score}")
                return

        for asteroid in asteroids:
            for bullet in shots:
                if Shot.collision(bullet, asteroid):
                    player.score += asteroid.score_amount
                    tools.update_text(score=player.score)
                    asteroid.split()
                    bullet.kill()

        for thing in drawable:
            thing.draw(screen)

        # draw score and tools displays
        tools.draw()

        clock.tick(60)
        dt = clock.get_time() / 1000
        pygame.display.flip()


if __name__ == "__main__":
    main()
