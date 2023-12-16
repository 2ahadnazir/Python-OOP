class Settings():

    def __init__(self):
        # initializing game setting
        self.screen_width = 720
        self.screen_length = 720
        self.bg_color = (25,0,51)

        self.ship_limit = 3


        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,150,160)
        self.bullet_allowed = 3

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 5
        self.fleet_direction = 1     # 1 for right  -1 for left

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

    def increase_speed(self):

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale


