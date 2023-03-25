'''
    store all the classes in Space-War-game
'''

import pygame

class Settings():
    def __init__(self):
        '''initialize the game settings'''
        # screen
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (0,100,200)

        # the speed of fighter
        self.ship_speed_factor = 0.5

        # bullets
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3


