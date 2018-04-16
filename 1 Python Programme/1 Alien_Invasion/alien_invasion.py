# package
import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats

## main

def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 存储游戏 统计信息的
    stats = GameStats(ai_settings)


    ship = Ship(ai_settings, screen)

    # 创建存储子弹的编组
    bullets = Group()

    # 创建外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)


    while True:

        ## 响应按键和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()

            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        ## 更新图像
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
