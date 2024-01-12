import pygame
from random import randint

class WitchHouse:
    def __init__(self, aad_game):
        """Initialize the witch house and set its position"""
        self.screen = aad_game.screen
        self.image = pygame.image.load('images/woodhouse.bmp')
        
        self.rect = self.image.get_rect()
        self.place_house()

    
    def blitme(self):
        """Draw witch house on the screen"""
        self.screen.blit(self.image, self.rect)

    def place_house(self):
        """Set the witch house at the top left of the screen"""
        self.rect.x = 0
        self.rect.y = 50
        