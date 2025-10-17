import pygame
from constants import PICKUP_MIN_SPAWN, PICKUP_MAX_SPAWN, SCREEN_WIDTH, SCREEN_HEIGHT, PICKUP_MAX
import random
from enum import Enum
from pygame import Vector2
from pickupshield import PickupShield

class PickupTypes(Enum):
    SHIELD = 1

class PickupHandler(pygame.sprite.Sprite):
    def __init__(self, pickups_group):
        super().__init__(self.containers)
        self.pickup_spawn = PICKUP_MAX_SPAWN
        self.pickups_group = pickups_group
    
    def spawn_random_pickup(self):
        from pickuphandler import PickupTypes
        all_pickups = [
            PickupTypes.SHIELD
        ]
        random_select: PickupTypes = random.choice(all_pickups)

        random_spawn_location = Vector2(
            random.uniform(0, 1) * SCREEN_WIDTH,
            random.uniform(0, 1) * SCREEN_HEIGHT
        )

        match random_select:
            case PickupTypes.SHIELD:
                PickupShield(random_spawn_location)

    def update(self, dt):
        print(len(self.pickups_group))
        if self.pickup_spawn > 0 and len(self.pickups_group) < PICKUP_MAX:
            self.pickup_spawn -= dt
        else:
            self.spawn_random_pickup()
            self.pickup_spawn = random.uniform(PICKUP_MIN_SPAWN, PICKUP_MAX_SPAWN)