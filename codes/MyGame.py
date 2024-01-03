import pygame
import subprocess
import sys
from codes import MyDefine
from codes.SpriteManager import SpriteManager
from codes.CharacterManager import CharacterManager
from codes.GameLevelManager import GameLevelManager
from codes.EventTriggerManager import EventTriggerManager
from codes.EventTrigger import EventTrigger


class MyGame(EventTrigger):

    def __init__(self):
        super().__init__()
        pygame.init()
        self.m_window = pygame.display.set_mode((MyDefine.GAME_RESOLUTION[0], MyDefine.GAME_RESOLUTION[1]))
        pygame.display.set_caption(MyDefine.GAME_NAME)
        self.m_clock = pygame.time.Clock()
        self.m_player = None
        self.m_running = False
        EventTriggerManager.get_instance().append_trigger(self)

    def start(self):
        GameLevelManager.get_instance().start(0)

    def run(self):
        # 游戏循环
        self.m_running = True
        while self.m_running:
            # 检查事件
            EventTriggerManager.get_instance().trigger()

            # Lock frame rate
            # self.m_clock.tick(MyDefine.GAME_FRAME_RATE)

            # 填充窗口为白色
            self.m_window.fill(MyDefine.BACKGROUND_COLOR)

            # 在窗口上绘制一些图形或精灵
            # 这里可以添加你自己的绘制逻辑，比如绘制角色、地图、物体等
            self.update()
            self.render()

            # 刷新屏幕
            pygame.display.flip()

    def update(self):
        CharacterManager.get_instance().update()
        SpriteManager.get_instance().update()

    def render(self):
        SpriteManager.get_instance().render(self.m_window)

    def end(self):
        pygame.quit()
        subprocess.run(["python", "CharacterChoose.py"])
        sys.exit()

    def trigger(self, event):
        if event.type == pygame.QUIT:
            self.m_running = False
