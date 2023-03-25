import sys
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
import game_function as gf


def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))  # the size of surface
    pygame.display.set_caption("Alien Invasion")

    # initialize a fighter ship
    ship = Ship(game_settings, screen)

    # initialize a group of bullets and aliens
    bullets = Group()
    aliens = Group()
    gf.create_fleet(game_settings, screen, ship, aliens)

    # intialize a alien
    # alien = Alien(game_settings, screen)


    # set the color of background
    bg_color = (0,100,200)

    # the main loop of the game
    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(game_settings, aliens)
        gf.update_screen(game_settings, screen, ship, aliens, bullets)


run_game()
