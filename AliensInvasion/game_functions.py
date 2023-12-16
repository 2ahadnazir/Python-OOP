import sys
import pygame
from bullet import Bullet
from Alien import Alien
from time import sleep


def fire_bullets(game_Settings, screen, ship, bullets):

    if len(bullets) < game_Settings.bullet_allowed:
        new_bullet = Bullet(game_Settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown_event(event, game_Settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # Move ship to the right
        # ship.rect.centerx += 6
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        # ship.rect.centerx -= 6
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_SPACE:
        fire_bullets(game_Settings, screen, ship, bullets)


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(game_Settings, screen, stats, play_button, aliens,  ship, bullets):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, game_Settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_X, mouse_Y = pygame.mouse.get_pos()
            check_play_button(game_Settings, screen, stats, play_button, ship, aliens, bullets, mouse_X, mouse_Y)

def check_play_button(game_Settings, screen, stats, play_button, ship, aliens, bullets, mouse_X, mouse_Y):


    button_clicked = play_button.rect.collidepoint(mouse_X, mouse_Y)
    if button_clicked and not stats.game_active:
        game_Settings.initialize_dynamic_settings()
        stats.game_active = True
        pygame.mouse.set_visible(False)

        aliens.empty()
        bullets.empty()

        create_fleet(game_Settings, screen, ship, aliens)
        ship.center_ship()



def update_screen(game_Settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(game_Settings.bg_color)

    # Redraw the bullet
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()


# alien.blitme()

def update_bullets(game_Settings, screen, ship, aliens, bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(game_Settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(game_Settings, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)  # If F,F (nothing will happens) T, T (Obj getting hit will be eliminated)

    # IF F,T ( bullet will continue to top even after destroying th
    if len(aliens) == 0:
        # Destroy existing bullets, speed up game, and create new fleet.
        bullets.empty()
        game_Settings.increase_speed()
        create_fleet(game_Settings, screen, ship, aliens)


def get_number_alien_x(game_Settings, alien_width):
    available_space_x = game_Settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(game_Settings, ship_height, alien_height):
    available_space_y = (game_Settings.screen_length - (2 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(game_Settings, screen, aliens, alien_number, row_number):
    alien = Alien(game_Settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(game_Settings, screen, ship, aliens):
    alien = Alien(game_Settings, screen)
    number_aliens_x = get_number_alien_x(game_Settings, alien.rect.width)
    number_rows = get_number_rows(game_Settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_Settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(game_Settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_Settings, aliens)
            break


def change_fleet_direction(game_Settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += game_Settings.fleet_drop_speed
    game_Settings.fleet_direction *= -1


def update_aliens(game_Settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(game_Settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollide(ship, aliens, dokill=1):
        # print(' !!!....Ship Hit....!!!')
        ship_hit(game_Settings, stats, screen, ship, aliens, bullets)
        check_aliens_bottom(game_Settings, stats, screen, ship, aliens, bullets)


def ship_hit(game_Settings, stats, screen, ship, aliens, bullets):
    if stats.ship_left > 0:
        # Decrese the ship after it hits
        stats.ship_left -= 1
        # empty the list of bullets and aliens
        aliens.empty()
        bullets.empty()
        # create a new fleet
        create_fleet(game_Settings, screen, ship, aliens)
        ship.center_ship()
        # Pause
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(game_Settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(game_Settings, stats, screen, ship, aliens, bullets)
            break
