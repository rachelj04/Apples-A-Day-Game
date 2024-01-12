from apple import Apple
from random import randint
import pygame
from pygame.sprite import Sprite

class PoisonApple(Apple):
    def __init__(self, aad_game):
        """Initialize poison apple"""
        self.poison_apples = aad_game.poison_apples
        super().__init__(aad_game)
        self.image = pygame.image.load('images/poison-apple.bmp')
        
        
    def place_apple(self):
        "Place poison apple randomly, avoid overlapping with other items"
        self.rect.left = randint(0, self.screen_rect.right - self.rect.width)
        self.rect.top = randint(50, self.screen_rect.bottom - self.rect.height)
        while (self.player_rect.colliderect(self.rect) or self.door_rect.colliderect(
            self.rect) or pygame.sprite.spritecollideany(self, 
            self.apples) or pygame.sprite.spritecollideany(self, self.poison_apples)):
            self.rect.left = randint(0, self.screen_rect.right - self.rect.width)
            self.rect.top = randint(50, self.screen_rect.bottom - self.rect.height)