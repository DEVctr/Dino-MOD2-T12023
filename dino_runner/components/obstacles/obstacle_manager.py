import pygame
import random
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.muto import Muto
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = [LARGE_CACTUS, SMALL_CACTUS, BIRD]
        self.obstacles = []

    def update(self, game):
        image_list = [Bird(), Muto()]
        if len(self.obstacles) == 0:
            self.obstacles.append(image_list[random.randint(0, 1)])
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    self.obstacles.remove(obstacle)
            '''elif game.player_2.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    self.obstacles.remove(obstacle)'''

    def reset_obstacles(self):
        self.obstacles = []
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)