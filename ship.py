import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        if self.moving_right and self.rect.x < 1630:
             self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.x> 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.y > 100:
            self.rect.y -= (self.ai_settings.ship_speed_factor-0.5)
        if self.moving_down and self.rect.y < 1010:
            self.rect.y += (self.ai_settings.ship_speed_factor-0.5)
        self.rect.centerx = self.center
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.x=700
        self.rect.y=1010
    def  blitme(self):
        self.screen.blit(self.image, self.rect)
