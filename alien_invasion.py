import sys
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_function as gf


def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))  # the size of surface
    pygame.display.set_caption("Alien Invasion")

    # initialize a fighter ship
    ship = Ship(game_settings, screen)

    # initialize a group of bullets
    bullets = Group()

    # set the color of background
    bg_color = (0,100,200)

    # the main loop of the game
    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        gf.update_screen(game_settings, screen, ship, bullets)
        # screen.fill(game_settings.bg_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        ship.blitme()
        pygame.display.flip()  # update the full display surface


run_game()
