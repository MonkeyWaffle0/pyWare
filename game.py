import pygame
from pygame.locals import *

from data.scripts.scenes.main_menu import MainMenu
from data.scripts.scenes.minigames.monkeyclicker import MonkeyClicker
from data.scripts.ui.fps import FPS
from data.scripts.ui.gui import GUI
from data.scripts.ui.user_input import InputManager

from data.scripts.entities.entity_manager import EntityManager
from data.scripts.window import GameWindow
from data.scripts.vfx.transitions import Transitions


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption('game base')

        self.difficulty = 'easy'

        self.window = GameWindow()
        self.input = InputManager(self)
        self.entities = EntityManager(self)
        self.gui = GUI(self)
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.transitions = Transitions(self)
        self.active_scene = MonkeyClicker(self)

        self.render_mode = 'game'

        self.running = True
        self.game_timer = 0

    def update(self):
        # self.fps.frame_begin()

        if self.render_mode == 'game':
            self.active_scene.handle_game_frame()

        if self.render_mode == 'transition':
            self.transitions.update()

        self.gui.update()
        # self.fps.frame_end()
        self.window.update(self)
        self.clock.tick(self.fps)

    def run(self):
        while self.active_scene is not None:
            self.update()

    def next_game(self):
        self.active_scene.next = MonkeyClicker(self)


if __name__ == '__main__':
    Game().run()
