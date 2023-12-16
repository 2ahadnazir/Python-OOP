import pygame
import game_functions as gf
from button import Button
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard

def run_game():
    # Initalize the game

    pygame.init()
    game_Settings = Settings()
    screen = pygame.display.set_mode((game_Settings.screen_width, game_Settings.screen_length))
    pygame.display.set_caption('Alien Invasion')
    # Make Play button
    play_button = Button(game_Settings, screen, 'PLAY')

    # instance to store game stats
    stats = GameStats(game_Settings)
    sb = Scoreboard(game_Settings, screen, stats)

    # Make a ship
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(game_Settings, screen, ship, aliens)

    while True:

        gf.check_events(game_Settings, screen, stats, play_button, aliens,  ship, bullets)


        if stats.game_active:
            ship.movement_update()
            gf.update_bullets(game_Settings, screen, ship, aliens, bullets)
            gf.update_aliens(game_Settings, stats, screen, ship, aliens, bullets)


        gf.update_screen(game_Settings, screen, stats, sb, ship, aliens, bullets, play_button)


        pygame.display.flip()

run_game()
