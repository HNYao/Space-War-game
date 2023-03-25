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


def create_fleet(game_settings, screen,ship, aliens):
    """set up a group of aliens"""
    alien = Alien(game_settings, screen)
    number_aliens_x = geu_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height, alien.rect.height)
    # print(number_aliens_x)

    # set up the first line of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)


def geu_number_aliens_x(game_settings, alien_width):
    available_space_x = game_settings.screen_width - 2 * alien_width
    return int(available_space_x / (2 * alien_width))


def create_alien(game_settings, screen, aliens, alien_num, row_number):
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_num
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(game_settings, ship_height, alien_height):
    """calculate the maximum number of rows"""
    available_space_y = (game_settings.screen_height - 3 * alien_height - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(game_settings, aliens):
    """update the aliens' positions"""
    check_fleet_edges(game_settings, aliens)
    aliens.update()

def check_fleet_edges(game_settings, aliens):
    """take reactions when aliens touch the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break


def change_fleet_direction(game_settings, aliens):
    """move the alien down and change its direction"""
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1









