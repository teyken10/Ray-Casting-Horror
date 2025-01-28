import math


class Settings:
    def __init__(self):
        # размеры экрана и частота кадров
        self.width = 1200
        self.height = 800
        self.half_width = self.width // 2
        self.half_height = self.height // 2
        self.fps = 165
        self.fps_pos = (self.width - self.width // 22, self.height // 160)
        self.tile = 100

        # громкость музыки и звуков
        self.volume_music = 50
        self.volume_sound = 50

        # настройки мини-карты
        self.map_scale = 5
        self.map_tile = self.tile // self.map_scale
        self.map_pos = (0, 0)

        # настройки ray casting
        self.fov = math.pi / 3
        self.half_fov = self.fov / 2
        self.num_rays = 300
        self.max_depth = 800
        self.delta_angle = self.fov / self.num_rays
        self.dist = self.num_rays / (2 * math.tan(self.half_fov))
        self.proj_coeff = 3 * self.dist * self.tile
        self.scale = self.width // self.num_rays

        # настройки спрайтов
        self.double_pi = 2 * math.pi
        self.center_ray = self.num_rays // 2 - 1

        # настройки текстур (1200 x 1200)
        self.texture_width = 1200
        self.texture_height = 1200
        self.texture_scale = self.texture_width // self.tile

        # настройки игрока
        self.player_pos = self.width // 2, self.height // 2
        self.player_angle = 0
        self.player_speed = 2
        self.rotate_speed = 0.02

        # цвета
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (220, 0, 0)
        self.green = (0, 220, 0)
        self.blue = (0, 0, 255)
        self.darkgray = (40, 40, 40)
        self.purple = (120, 0, 120)
        self.dark_yellow = (200, 200, 0)
        self.yellow = (255, 255, 0)
        self.skyblue = (0, 186, 255)
        self.sandy = (244, 164, 96)


settings = Settings()
