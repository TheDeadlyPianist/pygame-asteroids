import pygame
from circleshape import CircleShape
import random
from pygame import Vector2
from constants import ASTEROID_KINDS, ASTEROID_MIN_RADIUS
from colors import GREY


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, GREY, self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity.rotate(self.rotation) * dt)

    def take_hit(self):
        asteroid_tier = self.radius/ASTEROID_MIN_RADIUS

        if self.radius/ASTEROID_MIN_RADIUS > 1:
            split_direction = random.randint(10, 40)
            Asteroid.spawn_asteroid(self.position, self.velocity.rotate(-split_direction).normalize(), self.velocity.magnitude() * 1.2, asteroid_tier - 1)
            Asteroid.spawn_asteroid(self.position, self.velocity.rotate(split_direction).normalize(), self.velocity.magnitude() * 1.2, asteroid_tier - 1)

        self.kill()

    @staticmethod
    def spawn_asteroid(spawn_location: Vector2, movement_vector: Vector2, speed = None, asteroid_kind = None):
        if not speed:
            speed = random.randint(40, 100)
        if not asteroid_kind:
            asteroid_kind = random.randint(1, ASTEROID_KINDS)
        asteroid: Asteroid = Asteroid(spawn_location.x, spawn_location.y, ASTEROID_MIN_RADIUS * asteroid_kind)
        asteroid.velocity = movement_vector * speed