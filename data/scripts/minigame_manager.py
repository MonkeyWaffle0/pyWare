from random import choice

from data.scripts.scenes.minigames.monkeyclicker import MonkeyClicker


class MiniGameManager:
    def __init__(self, game):
        self.game = game
        self.game_list = [MonkeyClicker(game)]
        self.current_game = None

    def choose_game(self):
        chosen_game = choice(self.game_list)
        # TODO: uncomment when multiple games in the list
        # while chosen_game == self.current_game:
        #     chosen_game = choice(self.game_list)
        self.current_game = chosen_game
        return self.current_game

    def reset_current(self):
        self.current_game.__init__(self.game)

    def next_game(self):
        self.reset_current()
        self.game.active_scene = self.choose_game()
