import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('.\\images\\plane2\\plane2_03.png')
        self.image = pygame.transform.scale(self.image, (64,64))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性中存储浮点数值
        self.centerx = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # 设置飞船的速度系数
        self.speed_accelerate = 1

    def check_ship_position(self):
        """判断飞船的位置，用于飞行限位"""
        if self.centerx < 0:
            self.centerx = 0
        elif self.centerx > self.screen_rect.right:
            self.centerx = self.screen_rect.right
        if self.bottom > self.screen_rect.bottom:
            self.bottom = self.screen_rect.bottom
        elif self.bottom <  (2/3) * self.screen_rect.bottom:
            self.bottom = (2/3) * self.screen_rect.bottom

    def accelerate(self):
        self.speed_accelerate += 1

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center和bottom值，而非rect

        # #飞船飞行状态栏
        # print('moving_up:' + str(self.moving_up) + '   '  +  
        #       'moving_down:' + str(self.moving_down) + '   ' + 
        #       'moving_left:' + str(self.moving_left) + '   ' + 
        #       'moving_right:' + str(self.moving_right) + '   '
        #       ,end='\r')
        if self.moving_right and self.moving_up: # 右上方飞行
            self.image = pygame.image.load('.\\images\\plane2\\plane2_04.png')
            self.image = pygame.transform.scale(self.image, (64,64))
            self.centerx += self.ai_settings.ship_speed_factor * self.speed_accelerate
            self.bottom -= self.ai_settings.ship_speed_factor * self.speed_accelerate
        elif self.moving_right and self.moving_down: # 右下方飞行
            self.image = pygame.image.load('.\\images\\plane2\\plane2_04.png')
            self.image = pygame.transform.scale(self.image, (64,64))
            self.centerx += self.ai_settings.ship_speed_factor * self.speed_accelerate
            self.bottom += self.ai_settings.ship_speed_factor * self.speed_accelerate
        elif self.moving_left and self.moving_up: # 左上方飞行
            self.image = pygame.image.load('.\\images\\plane2\\plane2_03.png')
            self.image = pygame.transform.scale(self.image, (64,64))
            self.centerx -= self.ai_settings.ship_speed_factor * self.speed_accelerate
            self.bottom -= self.ai_settings.ship_speed_factor * self.speed_accelerate
        elif self.moving_left and self.moving_down: # 左下方飞行
            self.image = pygame.image.load('.\\images\\plane2\\plane2_03.png')
            self.image = pygame.transform.scale(self.image, (64,64))
            self.centerx -= self.ai_settings.ship_speed_factor * self.speed_accelerate
            self.bottom += self.ai_settings.ship_speed_factor * self.speed_accelerate
        elif self.moving_right: # 飞船对象的坐标值类型为int，若飞船移动的不长设置为浮点数，可能导致飞船无法向左或上移动
            self.image = pygame.image.load('.\\images\\plane2\\plane2_04.png')
            self.image = pygame.transform.scale(self.image, (64,64))
            self.centerx += self.ai_settings.ship_speed_factor * self.speed_accelerate
        elif self.moving_left:
            self.image = pygame.image.load('.\\images\\plane2\\plane2_02.png')
            self.image = pygame.transform.scale(self.image, (64,64))
            self.centerx -= self.ai_settings.ship_speed_factor * self.speed_accelerate
        elif self.moving_up:
            self.bottom -= self.ai_settings.ship_speed_factor * self.speed_accelerate
        elif self.moving_down:
            self.bottom += self.ai_settings.ship_speed_factor * self.speed_accelerate
        else:
            self.image = pygame.image.load('.\\images\\plane2\\plane2_03.png')
            self.image = pygame.transform.scale(self.image, (64,64))
        

        # 根据self.center更新rect对象
        self.rect.centerx = self.centerx
        self.rect.bottom = self.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom