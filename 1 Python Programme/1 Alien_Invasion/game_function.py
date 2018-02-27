## package

import sys
import pygame

## class
def check_events(ship):

    ## 响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('quit')
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):

    ## 更新屏幕上的颜色
    screen.fill(ai_settings.bg_color)
    ## 添加ship
    ship.blitme()

    ## 让最新的屏幕可见
    pygame.display.flip()





