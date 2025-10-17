from circleshape import CircleShape
from constants import BULLET_RADIUS, BULLET_SPEED
from pygame import Vector2
import pygame

class Bullet(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, BULLET_RADIUS)
        self.rotation = rotation

    def update(self, dt):
        self.position += Vector2(0, 1).rotate(self.rotation) * BULLET_SPEED * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 255), self.position, BULLET_RADIUS, 2)