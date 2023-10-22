import os
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
from imgs_load import AllImages


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    settings = Settings()
    # screen = pygame.display.set_mode((settings.screen_width, settings.screen_height), pygame.NOFRAME) # 无边框
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
 
    # 读取所有图像
    images = AllImages()
    images.get_plane_imgs(3)

    pygame.display.set_caption("Alien Invasion")
    icon_image = images.icon
    print(icon_image)
    pygame.display.set_icon(icon_image)

    # 创建Play按钮
    play_button = Button(settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats, images)

    # 设置游戏的背景色
    # bg_color = (230, 230, 230)

    # 加载背景图像
    background1 = images.bkground[0]
    background2 = images.bkground[1]
    background_y = 0
    # 设置背景滚动速度
    scroll_speed = 0.5

    # 放置一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(settings, screen, images)
    bullets = Group()
    aliens = Group()

    # 创建一个外星人群
    gf.create_fleet(settings, screen, ship, aliens)

    # 创建一个CLock对象
    clock = pygame.time.Clock()

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            # 飞船移动
            ship.check_ship_position()
            ship.update(images)
            gf.update_bullets(settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(settings, screen, stats, sb, ship, aliens, bullets)

        # 每次循环时都重绘屏幕
        background_y = gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button, background1, background2, background_y, scroll_speed)

        # 将游戏帧率锁定在100
        clock.tick(100)


if __name__ == '__main__':
    run_game()