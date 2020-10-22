class GUI:
    def __init__(self, game):
        self.game = game
        self.inventory_target_loc = 0
        self.inventory_loc = 0

    def render_overlay(self):
        pass

    def update(self):
        self.render_overlay()
        self.game.assets.font.render('fps: ' + str(int(sum(self.game.fps.fps_log) / len(self.game.fps.fps_log))),
                                     self.game.window.display, (2, 2))
