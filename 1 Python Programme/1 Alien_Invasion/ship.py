
import pygame

class Ship():
    def __init__(self, ai_settings, screen):

        self.screen = screen
        self.ai_setting = ai_settings

        self.image = pygame.image.load("images/feiji.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        ## 飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        ## 飞船属性center中存储小数值
        self.center = float(self.rect.centerx)

        ## 移动标志
        self.moving_right = False
        self.moving_left = False


    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        ## 根据标志调整飞船的位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.ai_setting.ship_speed_factor

    def center_ship(self):
        self.center = self.screen_rect.centerx