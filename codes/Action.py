import pygame
import pygame.image
from codes import MyDefine
from codes.ImageManager import ImageManager


class Action(pygame.sprite.Sprite):
    """"""

    def __init__(self):
        super().__init__()
        self.m_frames = []

    def loadAction(self, resName, actName, beginRow, beginCol, endRow, endCol):
        """Load action spirits"""
        res = ImageManager.getInstance().findResourceByName(resName)
        for i in range(endRow - beginRow):
            for j in range(endCol - beginCol):
                frame_surface = pygame.Surface(MyDefine.CHARACTER_RESOLUTION)
                frame_surface.blit(res[1], (0, 0), (i * MyDefine.CHARACTER_RESOLUTION[0],
                                                    j * MyDefine.CHARACTER_RESOLUTION[1],
                                                    MyDefine.CHARACTER_RESOLUTION[0],
                                                    MyDefine.CHARACTER_RESOLUTION[1]))
                self.m_frames.append(frame_surface)
