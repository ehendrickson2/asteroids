import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_BASE_SCORE


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.score_amount = ASTEROID_BASE_SCORE

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_score = self.score_amount * 2
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = vector1 * 1.2
        new_asteroid_2.velocity = vector2 * 1.2
        new_asteroid_1.score_amount = new_score
        new_asteroid_2.score_amount = new_score
