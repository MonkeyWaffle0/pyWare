from random import choice, randint

from data.scripts.config import GREEN, BLUE, RED, YELLOW, PURPLE, DISPLAY_SIZE, WHITE
from data.scripts.entities.buttons.monkeybutton import MonkeyButton
from data.scripts.scenes.minigames.minigame import MiniGame


class MonkeyClicker(MiniGame):
    def __init__(self, game, name='monkeyclicker'):
        super().__init__(game, name)
        self.i = 0   # Last button pressed
        # TODO: ajouter amount en variable dans les config
        self.buttons = [self.generate_button() for _ in range(10)]
        for i, button in enumerate(self.buttons):
            if i != self.i:
                button.active = False
                button.visible = False
        self.current = self.buttons[self.i]
        self.display = game.window.display
        # self.lives = [LifePoint(x * LifePoint.spacing) for x in range(1, 4)]

    def update(self):
        # Need to add a parameter for win/lose
        if self.is_lost():
            return self.lost()
        self.update_timebar()

    def next_button(self):
        self.i += 1
        if self.i == len(self.buttons):
            return self.win()
        self.current = self.buttons[self.i]
        self.current.enable_and_show()

    def lost_life(self):
        # self.lives.remove(self.lives[-1])
        pass

    def is_lost(self):
        if self.timebar.finished:
            return True
        else:
            return False

    def generate_button(self):
        width = randint(50, 100)
        height = randint(50, 100)
        x = randint(20, DISPLAY_SIZE[0] - (width + 50))
        y = randint(20, DISPLAY_SIZE[1] - (height + 50))
        return MonkeyButton(self.game, self.game.entities, 'button', x, y, width, height)
