import pygame
from pygame.sprite import Sprite

class Witch(Sprite):
    def __init__(self, aad_game):
        """Initialize the witch and place it at witch house"""
        super().__init__()
        self.screen = aad_game.screen
        self.settings = aad_game.settings
        self.image = pygame.image.load('images/witch.bmp')
        self.player = aad_game.player
        self.player_rect = self.player.rect
        self.image.set_colorkey((195, 195, 195))
        self.rect = self.image.get_rect()

        self.place_witch()
    

    def blitme(self):
        """Draw witch on the screen"""
        self.screen.blit(self.image, self.rect)
    

    def update(self):
        """Moving the witch towards the player"""
        if self.rect.centerx < self.player_rect.centerx:
            self.x += self.settings.witch_speed
            self.rect.x = self.x
        elif self.rect.centerx > self.player_rect.centerx:
            self.x -= self.settings.witch_speed
            self.rect.x = self.x

        if self.rect.centery < self.player_rect.centery:
            self.y += self.settings.witch_speed
            self.rect.y = self.y
        elif self.rect.centery > self.player_rect.centery:
            self.y -= self.settings.witch_speed
            self.rect.y = self.y
    

    def go_home(self):
        """Witch moving back to witch house"""
        if self.rect.x > 0:
            self.x -= self.settings.witch_speed
            self.rect.x = self.x
        
        if self.rect.y > 50:
            self.y -= self.settings.witch_speed
            self.rect.y = self.y
        
        
    def place_witch(self):
        """Place witch to witch house"""
        self.rect.x = 0
        self.rect.y = 50

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

