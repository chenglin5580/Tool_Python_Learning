
class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        ## 飞船移动速度
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        ## 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        ## 外星人
        self.alien_speed_factor = 1
        self.alien_drop_speed = 3
        # 1 表示右，-1表示左
        self.fleet_direction = 1

