from data.scripts.entities.buttons.startbutton import StartButton
from data.scripts.scenes.scene import Scene, DISPLAY_SIZE


class MainMenu(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.start_button = StartButton(game, game.entities, "button", DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] / 2, 50, 30)
        print(DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] / 2)

    def update(self):
        pass
