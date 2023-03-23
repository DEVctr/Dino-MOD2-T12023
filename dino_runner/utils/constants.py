import pygame
import math
import os

# Global Constants
TITLE = "Godzilla Runner"
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 1000
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
# Fazer função para animação do Guidorah e chamar no show_menu #
ICON = pygame.image.load(os.path.join(IMG_DIR, "Other/GodzillaDied.png"))
SETA = pygame.image.load(os.path.join(IMG_DIR, "Other/setas.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/godzillaRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/godzillaRun2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/godzillaRun3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/godzillaRun4.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/GodzillaNuclear1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/GodzillaNuclear2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/GodzillaNuclear3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/GodzillaNuclear4.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/GodzillaJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/GodzillaNuclear2.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/GodzillaDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/GodzillaDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/GodzillaNuclearDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/GodzillaNuclearDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/muto1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/muto2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/muto3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Rodan01.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Rodan02.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Rodan03.png")),
]

GUIDORAH = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Guidorah3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Guidorah2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Guidorah1.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/ogiva01.png'))
SHIELD_MENU = pygame.image.load(os.path.join(IMG_DIR, 'Other/ogivamenu.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BLACK = (0,0,0)
WHITE = (255,255,255)

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
FUNDO = pygame.image.load(os.path.join(IMG_DIR, 'Other/6.png'))
BACK = pygame.transform.scale(FUNDO, (SCREEN_WIDTH, SCREEN_HEIGHT - 110))

START = pygame.image.load(os.path.join(IMG_DIR, 'Other/startWhite.png'))
RESTART = pygame.image.load(os.path.join(IMG_DIR, 'Other/restartWhite.png'))
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOverWhite.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "atomic power"
