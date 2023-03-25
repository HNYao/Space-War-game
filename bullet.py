import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class for managing bullets"""

    def __init__(self, game_settings, screen, ship):
        """create a bullet instance in the ship position"""
        super().__init__()
        self.screen = screen

        # create a bullet rect in (0,0) and then set the correct positon
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # the possition of the bullet
        self.y = float(self.rect.y)
        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """move the bullet upwards"""
        self.y -=self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)