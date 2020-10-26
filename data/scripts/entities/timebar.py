import pygame

from data.scripts.config import GREEN, DISPLAY_SIZE
from data.scripts.entities.base_entities import GameEntity


class TimeBar(GameEntity):
    def __init__(self, game, entities, e_type, x, y, x_size, y_size, timer_max):
        super().__init__(game, entities, e_type, x, y, x_size, y_size)
        self.game = game
        self.x = x
        self.y = x
        self.percent = 100
        self.width = x_size
        self.height = y_size
        self.timer_max = timer_max
        self.color = GREEN
        self.timer = 0
        self.finished = False

    def new_frame(self):
        self.timer += 1
        self.percent = 1 - (self.timer / self.timer_max)
        self.width = DISPLAY_SIZE[0] * self.percent
        self.update_variable(self.x, self.y, self.width, self.height)
        if self.timer == self.timer_max:
            self.finished = True

    def update(self):
        pygame.draw.rect(self.game.window.display, self.color, (self.get_rect()))
