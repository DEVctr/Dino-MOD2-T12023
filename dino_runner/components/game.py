import pygame
import math
from dino_runner.utils.constants import BG, ICON, SETA, SHIELD_MENU, START, RESTART, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, BACK, GAME_OVER, BLACK, WHITE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.guidorah import Guidorah
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.powerups.power_up_manager import PowerUpManager
SCROLL = 0

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.death_count = 0
        self.game_speed = 5
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.guidorah = Guidorah()
        self.atomic_power = 0
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 10
        self.score = 0
        self.player.atomic_power = 0
        self.atomic_power = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 2

    def scroll(self):
        global SCROLL
        back_width = BACK.get_width()
        tiles = math.ceil(SCREEN_WIDTH / back_width + 50)
        for i in range(0, tiles):
            self.screen.blit(BACK, (i * back_width + SCROLL, 0))
        SCROLL -= 1
        if abs(SCROLL) > back_width:
            SCROLL = 0

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((0, 0, 0))
        self.scroll()
        self.draw_background()
        self.player.draw(self.screen)
        if self.score >= 1500 and self.score <= 1700:
            self.guidorah.draw(self.screen)
            if self.player.atomic_power >= 50:
                self.player.shield = True
                self.obstacle_manager.reset_obstacles()
        else:
            self.obstacle_manager.draw(self.screen)
            self.draw_score()
            self.draw_power_up_time()
            self.power_up_manager.draw(self.screen)
            
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed - 2

    def draw_score(self):
        draw_message_component(
            f"score: {self.score}",
            self.screen, BLACK,
            pos_x_center=900,
            pos_y_center=50
        )
        draw_message_component(
            f"atomic power: {self.player.atomic_power}",
            self.screen, BLACK,
            font_size=18,
            pos_x_center=100,
            pos_y_center=50
        )

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} enable for {time_to_show} seconds",
                    self.screen, BLACK,
                    font_size=18,
                    pos_x_center=500,
                    pos_y_center=40
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()
    
    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.screen.fill((BLACK))
            self.scroll()
            self.screen.blit(START, (half_screen_width - 180, half_screen_height))
            self.screen.blit(SETA, (half_screen_width - 120, half_screen_height + 30))
            self.screen.blit(SHIELD_MENU, (half_screen_width + 30, half_screen_height + 40))
        else:
            self.screen.fill((BLACK))
            self.scroll()
            self.screen.blit(RESTART, (half_screen_width - 180, half_screen_height + 180))
            draw_message_component(
                f"Your score: {self.score}", self.screen, WHITE,
                pos_y_center=half_screen_height - 150
            )
            draw_message_component(
                f"Your atomic power: {self.player.atomic_power}", self.screen, WHITE,
                pos_y_center=half_screen_height - 120
            )
            draw_message_component(
                f"Death count: {self.death_count}",
                self.screen, WHITE,
                pos_y_center=half_screen_height - 50
            )
            self.screen.blit(GAME_OVER, (half_screen_width - 190, half_screen_height - 200))
            self.screen.blit(ICON, (half_screen_width - 50, half_screen_height + 30))

        pygame.display.flip()
        
        self.handle_events_on_menu()
