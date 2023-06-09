"""
    game events
"""
import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(game_settings, screen, stats, sb,  play_button, ship, aliens, bullets):
    """reaction to keystrokes and clicks"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            print(event.type)
            check_keydown_events(event, game_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(game_settings, screen, stats, sb, play_button,ship, aliens, bullets, mouse_x, mouse_y):
    """start the game when player clicks the button"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # activate the game
        stats.game_active = True

        # hide the cursor
        pygame.mouse.set_visible(False)

        # reset the game
        stats.reset_stats()

        # reset the settings
        game_settings.initialize_dynamic_settings()

        # clean up the aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new fleet of aliens and reset the ship
        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()

        # reset the scoreboard
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()


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


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """update the image on the screen and switch to a new screen"""
    screen.fill(ai_settings.bg_color)

    # display the score
    sb.show_score()

    # redraw the bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # if inactive, draw the button
    if not stats.game_active:
        play_button.draw_button()

    # make the screen visible
    pygame.display.flip()


def update_bullets(game_settings, screen, stats, sb, ship, aliens, bullets):
    """update the bullet position and delete the invisible bullets"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(game_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(game_settings, screen, stats,sb, ship, aliens, bullets):
    # check collision
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        game_settings.increase_speed()
        create_fleet(game_settings, screen, ship, aliens)

        # level up
        stats.level += 1
        sb.prep_level()

    if collisions:
        for aliens in collisions.values():
            stats.score += game_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)


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


def update_aliens(game_settings, stats, screen, sb, ship, aliens, bullets):
    """update the aliens' positions"""
    check_fleet_edges(game_settings, aliens)
    aliens.update()

    # check the collisions between aliens and ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_settings, stats, screen, sb, ship, aliens, bullets)
        print("Warning: Ship hit!!!")

    # check if there are any aliens at the bottom
    check_aliens_bottom(game_settings, stats, screen, sb, ship, aliens, bullets)


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


def ship_hit(game_settings, stats, screen, sb, ship, aliens, bullets):
    """react to the collision between aliens and fighter"""
    # reduce the ship_left by 1
    if stats.ships_left > 0:
        stats.ships_left -= 1

        # clean up the aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new fleet
        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()

        # stop the game for a while
        sleep(0.5)

        # update scoreboard
        sb.prep_ships()

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(game_settings, stats, screen, sb, ship, aliens, bullets):
    """check if there are any aliens at the bottom"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(game_settings,stats,screen, sb, ship,aliens,bullets)
            break


def check_high_score(stats, sb):
    """check if there is a new best score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()










