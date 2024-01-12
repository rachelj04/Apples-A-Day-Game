import pygame
from pygame.sprite import Sprite
from random import randint

class Apple(Sprite):
    def __init__(self, aad_game):
        """Initialize apple"""
        super().__init__()
        self.screen = aad_game.screen
        self.screen_rect = aad_game.screen.get_rect()
        self.player = aad_game.player
        self.player_rect = self.player.rect
        self.door = aad_game.door
        self.door_rect = self.door.rect
        self.apples = aad_game.apples
        self.image = pygame.image.load('images/apple.bmp')
        self.rect = self.image.get_rect()
        self.place_apple()

    def place_apple(self):
        "Place apple randomly, avoid overlapping with other items"
        self.rect.left = randint(0, self.screen_rect.right - self.rect.width)
        self.rect.top = randint(50, self.screen_rect.bottom - self.rect.height)
        while (self.player_rect.colliderect(self.rect) or self.door_rect.colliderect(
            self.rect) or pygame.sprite.spritecollideany(self, self.apples)):
            self.rect.left = randint(0, self.screen_rect.right - self.rect.width)
            self.rect.top = randint(50, self.screen_rect.bottom - self.rect.height)

        