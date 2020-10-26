from data.scripts.entities.buttons.button import Button


class StartButton(Button):
    def __init__(self, game, entities, x, y, width, height):
        super().__init__(game, entities, x, y, width, height)

    def action(self):
        self.game.active_scene.switch_to(GameScene())
