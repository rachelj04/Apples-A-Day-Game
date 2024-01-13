import pygame
from pygame.sprite import Sprite
from random import randint

class Door(Sprite):
    def __init__(self, aad_game):
        """Initialize the door and place the door"""
        super().__init__()
        self.screen = aad_game.screen
        self.screen_rect = aad_game.screen.get_rect()

        self.image = pygame.image.load('images/door.bmp')
        self.rect = self.image.get_rect()
        self.player = aad_game.player
        self.player_rect = self.player.rect
        self.rect.x = 0
        self.rect.y = 50
        
    
    def blitme(self):
        """Draw door to the screen"""
        self.screen.blit(self.image, self.rect)

    def place_door(self):
        "Place door randomly, avoid overlapping with the player"
        self.rect.left = randint(0, self.screen_rect.right - self.rect.width)
        self.rect.top = randint(50, self.screen_rect.bottom - self.rect.height)
        while self.player_rect.colliderect(self.rect):
            self.rect.left = randint(0, self.screen_rect.right - self.rect.width)
            self.rect.top = randint(50, self.screen_rect.bottom - self.rect.height)
        