from pygame.sprite import Sprite
from pygame import Vector2
from constants import ASTEROID_MAX_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_SPAWN_RATE, ASTEROID_KINDS, ASTEROID_MIN_RADIUS
import random
from asteroid import Asteroid

class AsteroidField(Sprite):
    edges = [
        [
            Vector2(1, 0),
            lambda y_ratio: Vector2(-ASTEROID_MAX_RADIUS, y_ratio * SCREEN_HEIGHT)
        ],
        [
            Vector2(-1, 0),
            lambda y_ratio: Vector2(SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y_ratio * SCREEN_HEIGHT)
        ],
        [
            Vector2(0, 1),
            lambda x_ratio: Vector2(x_ratio * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS)
        ],
        [
            Vector2(0, -1),
            lambda x_ratio: Vector2(x_ratio * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS)
        ]
    ]

    def __init__(self):
        Sprite.__init__(self, self.containers)
        self.spawn_timer = 0

    def update(self, dt):
        self.spawn_timer -= dt
        if self.spawn_timer <= 0:
            self.spawn_asteroid()
            self.spawn_timer = ASTEROID_SPAWN_RATE

    def spawn_asteroid(self):
        spawn = random.choice(self.edges)

        movement_vector: Vector2 = spawn[0]
        movement_vector: Vector2 = movement_vector.rotate(random.randint(-30, 30))

        spawn_location: Vector2 = spawn[1](random.uniform(0, 1))

        Asteroid.spawn_asteroid(spawn_location, movement_vector)