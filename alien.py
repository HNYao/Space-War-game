import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class represents a single alien"""

    def __init__(self, game_settings, screen):
        """initialize the alien and its position"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        # load the image of alien and set rect
        self.image = pygame.image.load('images/ufo.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

        # alien's initial postition
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the exact  alien's position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw aliens in the specific position"""
        self.screen.blit(self.image, self.rect)


