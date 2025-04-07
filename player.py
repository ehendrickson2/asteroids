import pygame
import os

from circleshape import *
from tools import Tools
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_THRUST_ACCEL,
    SHOT_RADIUS,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
    BASE_PATH,
)


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.velocity = pygame.Vector2(0, 0)
        self.shoot_timer = 0
        self.score = 0
        self.image = pygame.image.load(
            os.path.join(BASE_PATH, "player_ship.png")
        ).convert_alpha()
        self.image = pygame.transform.scale(self.image, (45, 45))  # optional resize
        self.image = pygame.transform.rotate(self.image, 180)

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        rect = rotated_image.get_rect(center=self.position)

        screen.blit(rotated_image, rect.topleft)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, acceleration, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * acceleration * dt

    def shoot(self):
        bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        bullet.velocity = (
            pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        )

    def add_score(self, amount):
        self.score += amount
        Tools.update_text(self.score)

    def update(self, dt):
        self.velocity *= 0.99  # friction coefficent
        self.position += self.velocity * dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(PLAYER_THRUST_ACCEL, dt)
        if keys[pygame.K_s]:
            self.move(-PLAYER_THRUST_ACCEL, dt)
        if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
            self.shoot()
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        elif self.shoot_timer > 0:
            self.shoot_timer -= dt


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
