import pygame
import pygame.image
from codes import MyDefine


class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(
            MyDefine.CHARACTER_RESOLUTION)  # 创建一个矩形作为精灵图像
        self.image.fill((255, 0, 0))  # 填充为红色
        self.image = pygame.image.load(MyDefine.MAIN_ROLE_DIRECTORY)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # 初始位置在窗口中心
        num_frames_horizontal = self.image.get_width(
        ) // MyDefine.CHARACTER_RESOLUTION[0] // 4
        num_frames_vertical = self.image.get_height(
        ) // MyDefine.CHARACTER_RESOLUTION[1] // 2

        self.m_x = 0
        self.m_y = 0

    def update(self):
        # 这里可以添加精灵的更新逻辑
        pass
