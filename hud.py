import pygame
from constants import SCREEN_WIDTH
from colors import GREY
from pygame import Vector2
from pygame.font import SysFont
from colors import WHITE

class Hud(pygame.sprite.Sprite):

    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.score = 0

    def draw_text_element(self, screen, label: str, text: str, position: Vector2, deliminator: str = " "):
        base_font = SysFont("Comic Sans MS", 40)
        text_element = base_font.render(f"{label}{deliminator}{text}", True, WHITE)
        screen.blit(text_element, position)

    def draw(self, screen):
        surface = pygame.Surface((SCREEN_WIDTH, 50))
        surface.set_alpha(50)
        surface.fill(GREY)
        screen.blit(surface, (0, 0))

        self.draw_text_element(screen, "Score", str(self.score), Vector2(1100, 13))