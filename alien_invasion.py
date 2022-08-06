# allien invasion Game
import sys
import pygame
import game_function as gf

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    bullets = Group()

    aliens = Group()
    gf.creat_fleet(ai_settings,screen,ship,aliens)

    stats = GameStats(ai_settings)

    while True:

        gf.check_events(ai_settings,screen,ship,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, aliens,screen, ship,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
