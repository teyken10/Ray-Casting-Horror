import math


class Settings:
    def __init__(self):
        # настройки игры
        self.width = 1200
        self.height = 800
        self.half_width = self.width // 2
        self.half_height = self.height // 2
        self.penta_height = 5 * self.height
        self.double_height = 2 * self.height
        self.fps = 165
        self.fps_pos = (self.width - self.width // 22, self.height // 160)
        self.tile = 100
        self.reboot = True
        self.prehistory = False
        self.floor = 2
        self.change_floor = False
        self.end_game = False

        # громкость музыки и звуков
        self.volume_music = 0.5
        self.volume_sound = 0.5

        # настройки ray casting
        self.fov = math.pi / 3
        self.half_fov = self.fov / 2
        self.num_rays = 300
        self.max_depth = 800
        self.delta_angle = self.fov / self.num_rays
        self.dist = self.num_rays / (2 * math.tan(self.half_fov))
        self.proj_coeff = 5 * self.dist * self.tile
        self.scale = self.width // self.num_rays

        # настройки спрайтов
        self.double_pi = 2 * math.pi
        self.center_ray = self.num_rays // 2 - 1
        self.fake_rays = 100
        self.fake_rays_range = self.num_rays - 1 + 2 * self.fake_rays

        # настройки текстур (1200 x 1200)
        self.texture_width = 1200
        self.texture_height = 1200
        self.texture_scale = self.texture_width // self.tile

        # настройки игрока
        self.player_pos = self.half_width - 400, self.half_height + 450
        self.player_angle = 0
        self.player_speed = 165 / self.fps + 2
        self.sensitivity = 0.003

        # цвета
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (220, 0, 0)
        self.darkred = (40, 0, 0)
        self.green = (0, 220, 0)
        self.blue = (0, 0, 255)
        self.darkgray = (40, 40, 40)
        self.purple = (120, 0, 120)
        self.dark_yellow = (200, 200, 0)
        self.yellow = (255, 255, 0)
        self.skyblue = (0, 186, 255)
        self.sandy = (234, 118, 1)
        self.pink = (230, 1, 107)


settings = Settings()
