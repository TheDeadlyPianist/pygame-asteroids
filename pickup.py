import pygame
from circleshape import CircleShape
from pygame import Vector2
from constants import PICKUP_SHIELD_MIN_COEFFICIENT, PICKUP_SHIELD_PULSE_HOLD, PICKUP_LIFETIME

class Pickup(CircleShape):
    def __init__(self, location: Vector2, radius: float):
        super().__init__(location.x, location.y, radius)
        self.pulse_coeficcient = 1
        self.pulse_direction = -1
        self.pulse_hold = 0
        self.name = "Pickup Base"
        self.life = PICKUP_LIFETIME

    def pickup_action(self, player):
        pass

    def update(self, dt):
        if self.life > 0:
            self.life -= dt
        else:
            self.kill()

        if self.pulse_coeficcient > 1 and self.pulse_hold <= 0 and self.pulse_direction == 1:
            self.pulse_direction = -1
            self.pulse_hold = PICKUP_SHIELD_PULSE_HOLD
        elif self.pulse_coeficcient < PICKUP_SHIELD_MIN_COEFFICIENT and self.pulse_hold <= 0 and self.pulse_direction == -1:
            self.pulse_direction = 1
            self.pulse_hold = PICKUP_SHIELD_PULSE_HOLD

        if self.pulse_hold > 0:
            self.pulse_hold -= dt
        else:
            self.pulse_coeficcient += dt * self.pulse_direction * 0.2
