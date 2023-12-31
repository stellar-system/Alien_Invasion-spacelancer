class Settings():
    """存储游戏所有设置类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 400
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed_factor = 2
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 12
        self.bullet_width = 10
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # 外星人设置
        self.alien_speed_factor = 0.4
        self.fleet_drop_speed = 60
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1

        # 外星人提高点数的速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_facotr = 1
        self.bullet_speed_factor = 6
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右，为-1表示向左
        self.fleet_direction = 1

        # 计分
        self.alien_points = 1

    def increase_speed(self):
        """提高速度设置和外星人点数"""
        self.ship_speed_facotr *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
