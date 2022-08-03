# allien invasion Game
import sys
import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_function as gf


def run_game():
    pygame.init()
    ai_settings = Settings();
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_high))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    bullets = Group()

    while True:

        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()
