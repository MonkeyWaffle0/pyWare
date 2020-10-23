import pygame

from data.scripts.config import RED
from data.scripts.entities.base_entities import GameEntity


class Button(GameEntity):
    def __init__(self, game, entities, e_type, x, y, width, height):
        super().__init__(game, entities, e_type, x, y, width, height)
        self.game = game
        self.color = RED
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def action(self):
        print("you didn't override this in the child class")

    def check_clicked(self):
        if self.mouse_is_on() and self.game.input.left_click:
            return self.action()

    def update(self):
        self.check_clicked()
        pygame.draw.rect(self.game.window.display, self.color, self.rect)


class StartButton(Button):
    def __init__(self, game, entities, e_type, x, y, width, height):
        super().__init__(game, entities, e_type, x, y, width, height)

    def action(self):
        self.game.active_scene.switch_to(GameScene())
