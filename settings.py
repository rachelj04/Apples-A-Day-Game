class Settings:

    def __init__(self):
        """Initialize all game settings"""
        self.screen_width = 1000
        self.screen_height = 600
        # Set background color to Grey
        self.bg_color = (195, 195, 195)
        self.life_limit = 3
        self.apple_limit = 3

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.add_poison = 1
        self.initialize_dynamic_settings()
        

    def initialize_dynamic_settings(self):
        """Dynamic settings, which will change when level up"""
        self.player_speed = 1.5
        self.apple_points = 50
        self.poison_apple_limit = 1
        self.witch_speed = 0.1 # Witch speed is not increased 

    def increase_speed(self):
        """Update dynamic settings"""
        self.player_speed *= self.speedup_scale
        self.apple_points = int(self.apple_points * self.score_scale)
        self.poison_apple_limit += self.add_poison