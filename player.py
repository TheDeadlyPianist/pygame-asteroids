import pygame
from pygame import Vector2
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_MOVE_SPEED, SHOOT_COOLDOWN
from bullet import Bullet
from colors import WHITE, CYAN

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 180
        self.shot_cooldown = 0
        self.shield_level = 3

    def triangle(self):
        forward = Vector2(0, 1).rotate(self.rotation) * self.radius
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.3
        a = self.position + forward
        b = self.position - forward + right
        c = self.position - forward - right
        d = self.position - (forward/2)
        return [a, b, d, c]
    
    def draw_shield(self, screen):
        for i in range(1, self.shield_level + 1):
            pygame.draw.circle(screen, CYAN, self.position, self.radius + (i*7), 1)

    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)
        self.draw_shield(screen)

    def rotate(self, rotation):
        self.rotation += rotation

    def move(self, amount):
        forward = Vector2(0, 1).rotate(self.rotation)
        self.position += forward * amount

    def update(self, dt):
        if self.shot_cooldown > 0:
            self.shot_cooldown -= dt
        keys = pygame.key.get_pressed()

        rotation = PLAYER_TURN_SPEED * dt

        if keys[pygame.K_a]:
            self.rotate(rotation * -1)
        if keys[pygame.K_d]:
            self.rotate(rotation)
        if keys[pygame.K_w]:
            self.move(PLAYER_MOVE_SPEED * dt)
        if keys[pygame.K_s]:
            self.move(-PLAYER_MOVE_SPEED * dt)
        if keys[pygame.K_SPACE] and self.shot_cooldown <= 0:
            bullet_position: Vector2 = self.position + (Vector2(0, 1).rotate(self.rotation) * self.radius)
            Bullet(bullet_position.x, bullet_position.y, self.rotation)
            self.shot_cooldown = SHOOT_COOLDOWN

    def take_hit(self) -> bool:
        if self.shield_level > 0:
            self.shield_level -= 1
            return False
        return True