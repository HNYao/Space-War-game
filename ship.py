import pygame


class Ship():

    """class of the fighter ship"""

    def __init__(self,game_settings, screen):
        '''initialize the fighter and its position'''
        self.screen = screen
        self.game_settings = game_settings
        # load the fighter
        self.image = pygame.image.load('images/fighter.png')
        self.image = pygame.transform.scale(self.image,(60,60))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # set the new fighter at the bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #
        self.center = float(self.rect.centerx)

        # set a moving mark
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor

        self.rect.centerx = self.center


    def blitme(self):
        # draw the ship in the specific position
        self.screen.blit(self.image,self.rect)