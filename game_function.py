"""
    game events
"""
import pygame
import sys
from bullet import Bullet


def check_events(game_settins, screen, ship, bullets):
    """reaction to keystrokes and clicks"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settins, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, game_settings, screen, ship, bullets):
    """press the key"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # create a bullet
        fire_bullet(game_settings, screen, ship, bullets)



def check_keyup_events(event, ship):
    """release the key"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    """update the image on the screen and switch to a new screen"""
    screen.fill(ai_settings.bg_color)

    # redraw the bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    # make the screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """update the bullet positon and delete the invisible bullets"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

def fire_bullet(game_settings, screen, ship, bullets):
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)






