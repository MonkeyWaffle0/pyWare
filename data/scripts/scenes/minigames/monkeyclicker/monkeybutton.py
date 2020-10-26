from random import choice

from data.scripts.config import GREEN, BLUE, RED, YELLOW, PURPLE
from data.scripts.entities.buttons.button import Button


class MonkeyButton(Button):
    def __init__(self, game, entities, x, y, width, height):
        super().__init__(game, entities, x, y, width, height)
        colors = [GREEN, BLUE, RED, YELLOW, PURPLE]
        self.color = choice(colors)

    def check_clicked(self):
        if self.game.input.left_click and not self.game.active_scene.stop:
            self.game.input.left_click = False
            if self.mouse_is_on():
                return self.action()
            else:
                return self.game.active_scene.lost_life()

    def action(self):
        self.disable_and_hide()
        self.game.active_scene.next_button()
