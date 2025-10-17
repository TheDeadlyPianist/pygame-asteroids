import pygame
from pygame import Vector2
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: float):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.radius = radius
        self.out_of_bound_time = 2.0
        self.name = "CircleShape"
    
    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def move(self, amount):
        pass

    def collision(self, circle_object):
        distance_between = self.position.distance_to(circle_object.position)
        return distance_between < (self.radius + circle_object.radius)
    
    def remove_out_of_bounds(self, dt):
        if self.out_of_bound_time <= 0:
            self.kill()
        if self.position.x < -self.radius or self.position.x > SCREEN_WIDTH + self.radius or self.position.y < -self.radius or self.position.y > SCREEN_HEIGHT + self.radius:
            self.out_of_bound_time -= dt