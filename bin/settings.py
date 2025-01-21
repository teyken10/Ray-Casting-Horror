import math


class Settings:
    def __init__(self):
        self.width = 1400
        self.height = 800
        self.fps = 60
        self.volume_music = 50
        self.volume_sound = 50

settings = Settings()

# настройки игры
WIDTH = 1400
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100

# настройки ray casting
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 10
MAX_DEPTH = 1000
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# настройки игрока
player_pos = 0, 0

player_angle = 0
player_speed = 3
rotate_speed = 0.02

# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
DARK_YELLOW = (200,200,  0)
YELLOW = (255,255, 0)
