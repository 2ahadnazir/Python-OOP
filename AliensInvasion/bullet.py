import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, game_Settings, screen, ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0, game_Settings.bullet_width, game_Settings.bullet_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = game_Settings.bullet_color
        self.speed_factor = game_Settings.bullet_speed_factor


    def update(self):
            """Move the bullet up the screen."""
            # Update the decimal position of the bullet.
            self.y -= self.speed_factor
            # Update the rect position.
            self.rect.y = self.y

    def draw_bullet(self):
            """Draw the bullet to the screen."""
            pygame.draw.rect(self.screen, self.color, self.rect)