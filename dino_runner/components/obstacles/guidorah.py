from dino_runner.utils.constants import GUIDORAH
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_WIDTH

class Guidorah(Obstacle):
    def __init__(self):
        super().__init__(GUIDORAH, 0)
        self.rect.x = 800
        self.rect.y = 250
        self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 10], self.rect)
        self.step_index += 1

        if self.step_index >= 20:
            self.step_index = 0