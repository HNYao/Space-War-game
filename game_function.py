"""
    game events
"""
import pygame
import sys
from bullet import Bullet
from alien import Alien


def check_events(game_settins, screen, ship, bullets):
    """reaction to keystrokes and clicks"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            print(event.type)
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
    if event.key == pygame.K_q:
        # exit the game
        sys.exit()



def check_keyup_events(event, ship):
    """release the key"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """update the image on the screen and switch to a new screen"""
    screen.fill(ai_settings.bg_color)

    # redraw the bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
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

def create_fleet(game_settings, screen, aliens):
    """set up a group of aliens"""
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    print(number_aliens_x)

    # set up the first line of aliens
    for alien_number in range(number_aliens_x):
        alien = Alien(game_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)






