import pygame.font
from pygame.sprite import Group
from life import Life


class Scoreboard:
    """Class that shows the score infos"""
    def __init__(self, aad_game):
        """Initialize the scores"""
        self.aad_game = aad_game
        self.screen = aad_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = aad_game.settings
        self.stats = aad_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lives()
    

    def prep_score(self):
        """Get the current score, render to image, set at top right of the screen"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render("score: " + score_str, True, self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    
    def prep_high_score(self):
        """Get the highest score, render to image, set at midtop of the screen"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render("highest score: " + high_score_str, True, self.text_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def show_score(self):
        """Draw all scores on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.lives.draw(self.screen)
    
    def chech_high_score(self):
        """Update highest score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def prep_level(self):
        """Get the level, render to image, set under the score"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render("level: " + level_str, True, self.text_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    
    def prep_lives(self):
        """Set the lives left at top left of the screen"""
        self.lives = Group()
        for life_number in range(self.stats.lives_left):
            life = Life()
            life.rect.x = 10 + life_number * life.rect.width
            life.rect.y = 10
            self.lives.add(life)