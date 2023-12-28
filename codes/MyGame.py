import pygame
from codes import MyDefine


class MyGame:
    """Frame of this game"""

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(
            (MyDefine.GAME_RESOLUTION[0], MyDefine.GAME_RESOLUTION[1]))
        pygame.display.set_caption(MyDefine.GAME_NAME)

    def start(self):
        """Start this game"""

    def run(self):
        """Loop of the game"""
        # 游戏循环
        running = True
        while running:
            # 检查事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # 填充窗口为白色
            self.window.fill((255, 255, 255))

            # 在窗口上绘制一些图形或精灵
            self.do_logic()
            # 这里可以添加你自己的绘制逻辑，比如绘制角色、地图、物体等
            self.render()

            # 刷新屏幕
            pygame.display.flip()

    def end(self):
        """End this game"""
        pygame.quit()

    def do_logic(self):
        """Run logics in this method"""

    def render(self):
        """Render the frames in this method"""
