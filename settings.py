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
        self.ship_speed_factor = 1.5

