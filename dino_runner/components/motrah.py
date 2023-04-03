import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import (
    FLYING,
    UP,
    DOWN,
    DEFAULT_TYPE,
    SHIELD_TYPE,
    DOWN_SHIELD,
    UP_SHIELD,
    FLYING_SHIELD,
)

# MODIFICAR PARAMETROS E CONSTANTES

DOWN_IMG = {DEFAULT_TYPE: DOWN, SHIELD_TYPE: DOWN_SHIELD}
UP_IMG = {DEFAULT_TYPE: UP, SHIELD_TYPE: UP_SHIELD}
FLYING_IMG = {DEFAULT_TYPE: FLYING, SHIELD_TYPE: FLYING_SHIELD}
X_POS = 75
Y_POS = 160
Y_POS_DOWN = 200
UP_VEL = 7.5

class Motrah(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = FLYING_IMG[self.type][0]
        self.motrah_rect = self.image.get_rect()
        self.motrah_rect.x = X_POS
        self.motrah_rect.y = Y_POS
        self.step_index = 0
        self.motrah_fly = True
        self.motrah_up = False
        self.motrah_down = False
        self.up_vel = UP_VEL
        self.atomic_power = 0
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0

    def update(self, user_input):
        if self.motrah_fly:
            self.fly()
        elif self.motrah_up:
            self.up()
        elif self.motrah_down:
            self.down()
        if (
            user_input[pygame.K_UP]
            and not self.motrah_up
            or user_input[pygame.K_w]
            and not self.motrah_up
        ):
            self.motrah_fly = False
            self.motrah_up = True
            self.motrah_down = False
        elif (
            user_input[pygame.K_DOWN]
            and not self.motrah_up
            or user_input[pygame.K_s]
            and not self.motrah_up
        ):
            self.motrah_fly = False
            self.motrah_up = False
            self.motrah_down = True
        elif not self.motrah_up and not self.motrah_down:
            self.motrah_fly = True
            self.motrah_up = False
            self.motrah_down = False
        if self.step_index >= 15:
            self.step_index = 0

    def fly(self):
        self.image = FLYING_IMG[self.type][self.step_index // 5]
        self.motrah_rect = self.image.get_rect()
        self.motrah_rect.x = X_POS
        self.motrah_rect.y = Y_POS
        self.step_index += 1

    def up(self):
        self.image = UP_IMG[self.type]
        if self.motrah_up:
            self.motrah_rect.y -= self.up_vel * 4
            self.up_vel -= 0.8
        if self.up_vel < -UP_VEL:
            self.motrah_rect.y = Y_POS
            self.motrah_up = False
            self.up_vel = UP_VEL

    def down(self):
        self.image = DOWN_IMG[self.type]
        self.motrah_rect = self.image.get_rect()
        self.motrah_rect.x = X_POS
        self.motrah_rect.y = Y_POS_DOWN
        self.motrah_down = False

    def draw(self, screen):
        screen.blit(self.image, (self.motrah_rect.x, self.motrah_rect.y))
