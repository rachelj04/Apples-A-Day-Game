import pygame
from pygame.sprite import Sprite
from random import randint

class Player(Sprite):
    def __init__(self, aad_game):
        """Initialize the player and place the player"""
        super().__init__()
        self.screen = aad_game.screen
        self.settings = aad_game.settings
        self.screen_rect = aad_game.screen.get_rect()

        self.aad_game = aad_game

        self.image = pygame.image.load('images/girl.bmp')
        self.image.set_colorkey((195, 195, 195))
        self.rect = self.image.get_rect()

        self.center_player()
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    
    def update(self):
        """Update player's position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed
        if self.moving_up and self.rect.top > 50:
            self.y -= self.settings.player_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.player_speed
        
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        """Draw player to the screen"""
        self.screen.blit(self.image, self.rect)

    def center_player(self):
        """Place the player at midbottom of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    
    # def place_player(self):
    #     self.door = self.aad_game.door
    #     self.door_rect = self.door.rect
    #     self.apples = self.aad_game.apples
    #     self.poison_apples = self.aad_game.poison_apples
    #     self.rect.left = randint(0, self.screen_rect.right - self.rect.width)
    #     self.rect.top = randint(50, self.screen_rect.bottom - self.rect.height)
    #     while (self.door_rect.colliderect(self.rect) or pygame.sprite.spritecollideany(
    #         self, self.apples) or pygame.sprite.spritecollideany(self, self.poison_apples)):
    #         self.rect.left = randint(0, self.screen_rect.right - self.rect.width)
    #         self.rect.top = randint(50, self.screen_rect.bottom - self.rect.height)