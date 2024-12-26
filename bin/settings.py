import math

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
MAX_DEPTH = 1600
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# настройки игрока
player_pos = (HALF_WIDTH, HALF_HEIGHT)
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
