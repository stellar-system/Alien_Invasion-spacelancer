import sys
import pygame
from pygame.sprite import Group
from alien import Alien
from button import Button
from scoreboard import Scoreboard

from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf 


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 设置游戏的背景色
    bg_color = (230, 230, 230)

    # 放置一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建一个外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个CLock对象
    clock = pygame.time.Clock()

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            # 飞船移动
            ship.check_ship_position()
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

        # 将游戏帧率锁定在60
        clock.tick(300)

run_game()