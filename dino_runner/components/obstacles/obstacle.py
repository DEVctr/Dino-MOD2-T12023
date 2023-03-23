import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.size = fix_rect(self.rect.size, 0.73)
        self.rect.x = SCREEN_WIDTH
    
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed - 2
        if self.rect.x < -self.rect.width:
            obstacles.pop()
        
    def draw(self, screen):
        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))

def fix_rect(rect_size, factor):
    size = (
        rect_size[0] * factor,
        rect_size[1] * factor,
    )
    return size