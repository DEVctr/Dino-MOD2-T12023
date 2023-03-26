import pygame
from dino_runner.utils.constants import GODZILLA, GODZILLA_DAMAGE
from dino_runner.components.obstacles.obstacle import Obstacle

class GodzillaAtomic(Obstacle):
    def __init__(self):
        super().__init__(GODZILLA, 0)
        self.rect.x= 80
        self.rect.y = 330
        self.step_index = 0

    def draw(self, screen):
        self.time = pygame.time.get_ticks() + 5000
        if self.time:
            screen.blit(self.image[self.step_index // 1], self.rect)
            self.step_index += 1
        
            if self.step_index >= 18:
                self.step_index = 19


class GodzillaDamage(Obstacle):
    def __init__(self):
        super().__init__(GODZILLA_DAMAGE, 0)
        self.rect.x= 80
        self.rect.y = 330
        self.step_index = 0

    def draw(self, screen):
        self.time = pygame.time.get_ticks() + 5000
        if self.time:
            screen.blit(self.image[self.step_index // 10], self.rect)
            self.step_index += 1

            if self.step_index >= 20:
                self.step_index = 0