import sys
import pygame
from time import sleep

from player import Player
from settings import Settings
from button import Button
from scoreboard import Scoreboard
from game_stats import GameStats
from door import Door
from apple import Apple
from poison_apple import PoisonApple
from witch import Witch
from witch_house import WitchHouse


class ApplesADay:
    """Class to manage Apples-A-Day game"""
    def __init__(self):
        """Initailize the game"""
        pygame.init()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Apples A Day")
        self.player = Player(self)
        self.player_rect = self.player.rect
        self.door = Door(self)
        self.door_rect = self.door.rect
        self.witch_house = WitchHouse(self)
        self.witch_house_rect = self.witch_house.rect
        self.play_button = Button(self, "Play")
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.apples = pygame.sprite.Group()
        self.poison_apples = pygame.sprite.Group()
        self.witch = Witch(self)
        self.witch_rect = self.witch.rect
        self._create_foods()
        self._create_poisons()
   

    def run_game(self):
        """Run game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self._update_player()
                self._update_door()
                self._update_witch()
                self._update_poisons()
                self._update_apples()
            self._update_screen()


    def _check_events(self):
        """Check user inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Set the player movement or stop the game when key is pressed"""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_UP:
            self.player.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        """Stops player movement to a direction when that key is up"""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False
        elif event.key == pygame.K_UP:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = False

    
    def _check_play_button(self, mouse_pos):
        """If play button is clicked when game is not active, active new game"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_status()
            self.stats.game_active = True
            self.stats.witch_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_lives()
            self.player.center_player()
            self.witch.place_witch()
            pygame.mouse.set_visible(False)
    

    def _update_player(self):
        """Updates player position and status"""
        self.player.update()
        if (self.player_rect.right <= self.witch_house_rect.right and self.player_rect.bottom 
            <= self.witch_house_rect.bottom):
            self.stats.player_hided = True
        else:
            self.stats.player_hided = False



    def _update_door(self):
        """Game level up if the player enters the door"""
        if self.player_rect.collidepoint(self.door_rect.center):
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
            sleep(0.5)
            self.door.place_door()
            self.stats.witch_active = True
            self.apples.empty()
            self.poison_apples.empty()
            self._create_foods()
            self._create_poisons()
    
    def _update_witch(self):
        """Update witch behavior and change game status if witch catches the player"""
        if not self.stats.player_hided:
            if self.stats.witch_active:
                self.witch.update()
            else: 
                self.witch.go_home()
        
        if self.player_rect.collidepoint(self.witch_rect.center):
            if self.stats.lives_left > 0:
                self.stats.lives_left -= 1
                self.sb.prep_lives()
                self.player.center_player()
                sleep(0.5)
                self.stats.witch_active = False
            else:
                self.stats.game_active = False
                sleep(0.5)
                pygame.mouse.set_visible(True)
    
    def _create_foods(self):
        """Create apples"""
        for apple_number in range(self.settings.apple_limit):
            apple = Apple(self)
            self.apples.add(apple)
    

    def _update_apples(self):
        """Change game status if player eats apple"""
        collisions = pygame.sprite.spritecollide(self.player, self.apples, True)
        if collisions:
            for apple in collisions:
                self.stats.score += self.settings.apple_points
            self.sb.prep_score()
            self.sb.chech_high_score()
    
    def _create_poisons(self):
        """Create poison apples"""
        for poison_apple_number in range(self.settings.poison_apple_limit):
            poison_apple = PoisonApple(self)
            self.poison_apples.add(poison_apple)

    def _update_poisons(self):
        """Change game status if player eats poison apple"""
        collisions = pygame.sprite.spritecollide(self.player, self.poison_apples, True)
        if collisions:
            for poison_apple in collisions:
                if self.stats.lives_left > 0:
                    self.stats.lives_left -= 1
                    self.sb.prep_lives()
                else:
                    self.stats.game_active = False
                    pygame.mouse.set_visible(True)
    

    def _update_screen(self):
        """Draw all items on screen"""
        self.screen.fill(self.settings.bg_color)

        self.player.blitme()
        self.door.blitme()
        self.apples.draw(self.screen)
        self.poison_apples.draw(self.screen)
        self.witch.blitme()
        self.witch_house.blitme()
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()


if __name__ == '__main__':
    aad = ApplesADay()
    aad.run_game()