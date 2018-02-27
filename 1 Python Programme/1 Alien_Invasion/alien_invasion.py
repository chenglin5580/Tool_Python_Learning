# package
import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group

## main

def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.scree_height))
    pygame.display.set_caption("Alien Invasion")


    ship = Ship(ai_settings, screen)

    # 创建存储子弹的编组
    bullets = Group()


    for step in range(5000):

        ## 响应按键和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()

        gf.update_bullets(bullets)

         ## 更新图像
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()

