import pygame

class Ship():
    def __init__(self, screen):

        self.screen = screen

        # Load the ship and get it's rect

        self.image = pygame.image.load('rocket.bmp')
        self.image = pygame.transform.smoothscale(self.image, (50, 95))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Ship movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


        # Start each ship from the center of screen

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):

        self.screen.blit(self.image, self.rect)


    def movement_update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        elif self.moving_left and self.rect.left > 0 :
            self.rect.centerx -= 1
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 1
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self. rect.centery += 1

    def center_ship(self):
        self.center = self.screen_rect.centerx


