class GameStats:
    """Class store game status"""
    def __init__(self, aad_game):
        self.settings = aad_game.settings
        self.reset_status()
        self.game_active = False
        self.witch_active = True
        self.player_hided = False
        self.high_score = 0
        

    def reset_status(self):
        """Reset status when new game start"""
        self.lives_left = self.settings.life_limit
        self.score = 0
        self.level = 1