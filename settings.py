class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # ship speed factor
        self.ship_speed_factor = 1.5

        # bullet feature
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 2
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3

        # alien feature
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 2
        self.fleet_direction = 1