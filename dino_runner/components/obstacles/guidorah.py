from dino_runner.utils.constants import GUIDORAH_DAMAGE, GUIDORAH_ATTACK
from dino_runner.components.obstacles.obstacle import Obstacle

class GuidorahAttack(Obstacle):
    def __init__(self):
        super().__init__(GUIDORAH_ATTACK, 0)
        self.rect.x = 150
        self.rect.y = 250
        self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1

        if self.step_index >= 60:
            self.step_index = 45
            if self.step_index >= 60:
                self.step_index += 1

class GuidorahDamage(Obstacle):
    def __init__(self):
        super().__init__(GUIDORAH_DAMAGE, 0)
        self.rect.x = 780
        self.rect.y = 250
        self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 10], self.rect)
        self.step_index += 1

        if self.step_index >= 30:
            self.step_index = 0