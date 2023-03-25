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

    def update(self, *args: any, **kwargs: any) -> None:
        """move the alien towards right"""
        self.x += self.game_settings.alien_speed_factor * self.game_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """ if aliens touch the edge, return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True



