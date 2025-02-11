class Settings():
    def __init__(self):
        self.screen_width = 1600
        self.screen_height = 1000
        self.bg_color = (255,255,255)
        self.ship_limit = 3
        self.bullets_allowed = 10
        self.fleet_drop_speed = 20
        self.speedup_scale = 1
        self.score_scale = 1
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 2.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1.5
        self.fleet_direction = 1
        self.alien_points = 50
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)