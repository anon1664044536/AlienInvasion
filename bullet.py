import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Bullet,self).__init__()
        self.screen = screen
        self.image = pygame.image.load('./images/snow.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.rect.x += 9
        self.rect.y += 34
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        self.y -= self.speed_factor
        self.rect.y  = self.y
    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)