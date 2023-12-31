import pygame
import pygame.image
import math
import time
from codes import MyDefine
from codes.ImageManager import ImageManager

# Basic action frequency (f/s)
BASIC_ACTION_FREQUENCY = 4


class Action(pygame.sprite.Sprite):
    """Subclass of Sprite"""

    def __init__(self):
        super().__init__()
        self.m_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
        self.m_frames = []
        self.m_index = 0
        self.image = None
        self.rect = None

    def load_action(self, resName, actName, beginRow, beginCol, endRow, endCol):
        """Load action spirits"""
        res = ImageManager.get_instance().find_resource_by_name(resName)
        for i in range(endRow - beginRow):
            for j in range(endCol - beginCol):
                frame_surface = pygame.Surface(MyDefine.CHARACTER_RESOLUTION)
                frame_surface.blit(res[1], (0, 0), (i * MyDefine.CHARACTER_RESOLUTION[0],
                                                    j * MyDefine.CHARACTER_RESOLUTION[1],
                                                    MyDefine.CHARACTER_RESOLUTION[0],
                                                    MyDefine.CHARACTER_RESOLUTION[1]))
                self.m_frames.append(frame_surface)

    def update(self):
        curSec = MyDefine.convert_nsec_to_msec(time.time_ns())
        if math.floor(BASIC_ACTION_FREQUENCY * (curSec - self.m_sec) / 1000) > 0:
            self.m_index = (self.m_index + 1) % len(self.m_frames)
            self.m_sec = curSec
        self.image = self.m_frames[self.m_index]

    def set_center_pos(self, x, z):
        self.rect = self.image.get_rect()
        self.rect.center = (x, z)
