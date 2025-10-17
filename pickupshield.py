from pickup import Pickup
import pygame
from colors import CYAN
from constants import PICKUP_SHIELD_MAX_RADIUS, PLAYER_MAX_SHIELD
from player import Player

class PickupShield(Pickup):
    def __init__(self, location):
        super().__init__(location, PICKUP_SHIELD_MAX_RADIUS)
        self.name = "Pickup Shield"

    def draw(self, screen):
        pygame.draw.circle(screen, CYAN, self.position, self.radius * self.pulse_coeficcient, 2)

    def pickup_action(self, player: Player):
        if player.shield_level < PLAYER_MAX_SHIELD:
            player.shield_level += 1
            self.kill()