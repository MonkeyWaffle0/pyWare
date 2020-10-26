import pygame

from data.scripts.config import DISPLAY_SIZE, RED
from data.scripts.entities.base_entities import GameEntity


class LifePoint(GameEntity):
    def __init__(self, game, entities, x, y=DISPLAY_SIZE[1] - 50, e_type='lifepoint', width=40, height=40):
        super().__init__(game, entities, e_type, x, y, width, height)
        self.game = game
        self.display = game.window.display
        self.x = x
        self.y = y
        self.width = self.height = width
        self.color = RED

    def update(self):
        pygame.draw.rect(self.display, self.color, (self.get_rect()))
