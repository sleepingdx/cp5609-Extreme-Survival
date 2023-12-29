import pygame
from codes import MyDefine
from codes.Character import Character


class MyGame:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(
            (MyDefine.GAME_RESOLUTION[0], MyDefine.GAME_RESOLUTION[1]))
        pygame.display.set_caption(MyDefine.GAME_NAME)
        self.alql_sprites = pygame.sprite.Group()

        self.m_player = None

    def start(self):
        # Characters
        self.m_player = Character()
        self.all_sprites.add(self.m_player)

    def run(self):
        # 游戏循环
        running = True
        while running:
            # 检查事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # 填充窗口为白色
            self.window.fill(MyDefine.BACKGROUND_COLOR)

            # 在窗口上绘制一些图形或精灵
            # 这里可以添加你自己的绘制逻辑，比如绘制角色、地图、物体等
            self.update()
            self.render()

            # 刷新屏幕
            pygame.display.flip()

    def update(self):
        self.all_sprites.update()

    def render(self):
        self.all_sprites.draw(self.window)

    def end(self):
        pygame.quit()
