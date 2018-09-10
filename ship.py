import pygame

class Ship():
    def __init__( self, ai_settings, screen ):
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像，并获取其外形矩形
        self.image = pygame.image.load('images/ship1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #放在屏幕底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #属性center中存储小数值
        self.center = float ( self.rect.centerx )

        #移动 初始时
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ 根据移动目标调整位置 """
        #更新center值，而不是rect
        if  self.moving_right and self.rect.right < self.screen_rect.right:
            self.center +=self.ai_settings.ship_speed_factor
        if  self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image , self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中 """
        self.center = self.screen_rect.centerx
