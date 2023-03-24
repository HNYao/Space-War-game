import sys
import pygame
from settings import Settings


def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))  # the size of surface
    pygame.display.set_caption("Alien Invasion")

    # set the color of background
    bg_color = (0,100,200)
    screen.fill(game_settings.bg_color)

    # the main loop of the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip() # update the full display surface


run_game()
