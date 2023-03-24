"""
    game events
"""
import pygame
import sys

def check_events(ship):
    """reaction to keystrokes and clicks"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # move the ship towards right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """update the image on the screen and switch to a new screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # make the screen visible
    pygame.display.flip()





