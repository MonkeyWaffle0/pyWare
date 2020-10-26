from random import randint

from data.scripts.config import DISPLAY_SIZE, MINIGAMES
from data.scripts.scenes.minigames.monkeyclicker.lifepoint import LifePoint
from data.scripts.scenes.minigames.monkeyclicker.monkeybutton import MonkeyButton
from data.scripts.scenes.minigames.minigame import MiniGame


class MonkeyClicker(MiniGame):
    def __init__(self, game, name='monkeyclicker'):
        super().__init__(game, name)
        self.i = 0  # Last button pressed
        self.buttons = [self.generate_button() for _ in range(MINIGAMES[name][game.difficulty]['amount'])]
        for i, button in enumerate(self.buttons):
            if i != self.i:
                button.active = False
                button.visible = False
        self.current = self.buttons[self.i]
        self.display = game.window.display
        self.lives = [LifePoint(self.game, self.game.entities, x * DISPLAY_SIZE[0] * 0.1) for x in range(1, 4)]
        self.stop = False

    def update(self):
        self.update_timebar()
        if (self.timebar.finished or not self.lives) and not self.stop:
            self.stop = True
            return self.lose()

    def next_button(self):
        self.i += 1
        if self.i == len(self.buttons):
            return self.win()
        self.current = self.buttons[self.i]
        self.current.enable_and_show()

    def lost_life(self):
        self.game.entities.entities.remove(self.lives[-1])
        self.lives.remove(self.lives[-1])

    def generate_button(self):
        width = randint(50, 100)
        height = randint(50, 100)
        x = randint(20, DISPLAY_SIZE[0] - (width + 50))
        y = randint(20, DISPLAY_SIZE[1] - (height + 50))
        return MonkeyButton(self.game, self.game.entities, x, y, width, height)
