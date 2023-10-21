import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.ai_settings.bg_color = (0, 0, 0)

        # 显示得分信息时使用的字体设置
        self.text_color = (178, 34, 34)
        self.font = pygame.font.Font(".\GajrajOne-Regular.ttf", 30)
        self.text_top = 10

        # 准备包含最高得分和当前得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        round_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.text_top
        self.score_image.set_colorkey(self.ai_settings.bg_color)

    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将最高得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.text_top
        self.high_score_image.set_colorkey(self.ai_settings.bg_color)

    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render('Lv: '+  str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        self.level_image.set_colorkey(self.ai_settings.bg_color)

    def prep_ships(self):
        """显示还余下多少艘飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

        # 修改为飞船图标x剩余生命数量的格式
        ship_icon = pygame.image.load('.\\images\\planes\\plane2\\plane2_03.png') 
        self.ship_icon = pygame.transform.scale(ship_icon, (48, 48))
        self.ship_icon_rect = ship_icon.get_rect()
        self.ship_icon_rect.x = 10
        self.ship_icon_rect.y = 10
        self.screen.blit(ship_icon, self.ship_icon_rect)
        remaining_ships_text = f"x {self.stats.ships_left}"
        self.remaining_ships_image = self.font.render(remaining_ships_text, True, self.text_color, self.ai_settings.bg_color)
        self.remaining_ships_rect = self.remaining_ships_image.get_rect()
        self.remaining_ships_rect.x = self.ship_icon_rect.x + self.ship_icon_rect.width + 10
        self.remaining_ships_rect.y = self.text_top
        self.screen.blit(self.remaining_ships_image, self.remaining_ships_rect)
        self.remaining_ships_image.set_colorkey(self.ai_settings.bg_color)

    def show_score(self):
        """屏幕上显示飞船和得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ship_icon, self.ship_icon_rect)
        self.screen.blit(self.remaining_ships_image, self.remaining_ships_rect)
        # 绘制飞船
        # self.ships.draw(self.screen)