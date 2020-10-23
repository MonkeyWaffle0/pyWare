import pygame
import sys
from pygame.locals import *

from data.scripts.config import *


class InputManager:
    def __init__(self, game):
        self.game = game
        self.right = False
        self.left = False
        self.down_press = False
        self.interact = False
        self.jump = False
        self.down = False
        self.attempting_climb = False
        self.up = False
        self.left_click = False

        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_pos = [self.mouse_pos[0] / DISPLAY_SCALE, self.mouse_pos[1] / DISPLAY_SCALE]

    def reset(self):
        self.right = False
        self.left = False
        self.down_press = False
        self.interact = False
        self.jump = False
        self.down = False
        self.attempting_climb = False
        self.up = False
        self.left_click = False

    def get_updates(self):
        self.interact = False
        self.down_press = False
        self.jump = False
        self.attempting_climb = False
        self.left_click = False

        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_pos = [self.mouse_pos[0] / DISPLAY_SCALE, self.mouse_pos[1] / DISPLAY_SCALE]

        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE or (event.key == pygame.K_F4 and alt_pressed):
                    quit_attempt = True

            if quit_attempt:
                self.game.active_scene.terminate()

            self.just_clicked = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.jump = True
                if event.key == K_d:
                    self.right = True
                if event.key == K_a:
                    self.left = True
                if event.key == K_s:
                    self.down = True
                    self.down_press = True
                if event.key == K_w:
                    self.attempting_climb = True
                    self.up = True
                if event.key == K_e:
                    self.interact = True
            if event.type == KEYUP:
                if event.key == K_d:
                    self.right = False
                if event.key == K_a:
                    self.left = False
                if event.key == K_s:
                    self.down = False
                if event.key == K_w:
                    self.up = False
            if event.type == MOUSEBUTTONDOWN:
                self.left_click = True
            if event.type == MOUSEBUTTONUP:
                self.just_clicked = True
                self.left_click = False
