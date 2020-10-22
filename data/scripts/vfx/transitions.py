import pygame
from data.scripts.config import *
from data.scripts.core_funcs import *

TRANSITION_TYPES = {
    'startvillage>house': 'enter',
    'house>startvillage': 'exit',
}


class Transitions:
    def __init__(self, game):
        self.game = game
        self.time_remaining = 0
        self.type = None

    def start_transition(self, leaving, entering):
        transition_str = leaving + '>' + entering
        self.time_remaining = 60
        self.max_time = self.time_remaining
        self.type = TRANSITION_TYPES[transition_str]
        self.reloaded_map = False

    def update(self):

        self.time_remaining -= 1
        if self.time_remaining <= 0:
            self.game.render_mode = 'game'

        self.game.handle_game_frame()

        if (not self.reloaded_map) and (self.time_remaining < self.max_time / 2):
            self.game.level.load_map(self.game.level.transition_info[0])
            # level load callback for level start operations
            self.game.level.transition_info[1]()
            self.reloaded_map = True

        # exit and enter have the same animation
        if self.type == 'exit':
            self.type = 'enter'

        if self.type == 'enter':
            mask_surf = pygame.Surface(DISPLAY_SIZE)

            if self.time_remaining / self.max_time >= 0.5:
                pygame.draw.circle(mask_surf, (255, 255, 255), get_center_pos(self.game.window.display),
                                   ((self.time_remaining - self.max_time / 2) / (self.max_time / 2)) ** 4 * DISPLAY_SIZE[0])
            else:
                pygame.draw.circle(mask_surf, (255, 255, 255), get_center_pos(self.game.window.display),
                                   (1 - (self.time_remaining / (self.max_time / 2))) ** 4 * DISPLAY_SIZE[0])

            mask_surf.set_colorkey((255, 255, 255))
            self.game.window.display.blit(mask_surf, (0, 0))
