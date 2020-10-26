from data.scripts.config import MINIGAMES, DISPLAY_SIZE
from data.scripts.entities.timebar import TimeBar
from data.scripts.scenes.scene import Scene


class MiniGame(Scene):
    def __init__(self, game, name):
        super().__init__(game)
        self.name = name
        self.game = game
        self.timebar = self.create_timebar(MINIGAMES[name][game.difficulty]['timermax'])

    def create_timebar(self, max_time):
        return TimeBar(self.game, self.game.entities, "timebar", 0, 0, DISPLAY_SIZE[0], 20, max_time)

    def update_timebar(self):
        self.timebar.new_frame()

    def win(self):
        self.game.transitions.start_transition()
        self.game.render_mode = 'transition'

    def lose(self):
        print('WESH')
        self.game.transitions.start_transition()
        self.game.render_mode = 'transition'

    def reset(self):
        self.__init__(self.game, self.name)
