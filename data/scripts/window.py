import pygame

from data.scripts.config import *


class GameWindow:
    def __init__(self):
        self.screen = pygame.display.set_mode([DISPLAY_SIZE[0] * DISPLAY_SCALE, DISPLAY_SIZE[1] * DISPLAY_SCALE], 0, 32)

        self.display = pygame.Surface(DISPLAY_SIZE)
        self.size = DISPLAY_SIZE

    def update(self, game):
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
        pygame.display.update()
        game.clock.tick(60)
