import pygame
import pygame.image
import math
import time
from codes import MyDefine
from codes.ImageManager import ImageManager
from codes.Vector import Vector

# Basic action frequency (f/s)
BASIC_ACTION_FREQUENCY = 4
ACTION_ORIENTATION = ["Up", "Right", "Down", "Left"]
ACTION_VECTORS = [Vector(0, -1), Vector(1, 0), Vector(0, 1), Vector(-1, 0)]


class Action(pygame.sprite.Sprite):
    """Subclass of Sprite"""

    def __init__(self, obj):
        super().__init__()
        self.m_object = obj
        self.m_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
        self.m_frames = {
            ACTION_ORIENTATION[0]: [],
            ACTION_ORIENTATION[1]: [],
            ACTION_ORIENTATION[2]: [],
            ACTION_ORIENTATION[3]: [],
        }
        self.m_orientation = 0
        self.m_frame_index = 0
        self.image = None
        self.rect = None

    def load_action_by_index(self, actionName, orientationName, beginRow, beginCol, endRow, endCol):
        res = ImageManager.get_instance().find_resource_by_name(actionName)
        for i in range(endRow - beginRow):
            for j in range(endCol - beginCol):
                frame_surface = pygame.Surface(MyDefine.CHARACTER_RESOLUTION)
                frame_surface.blit(res[1], (0, 0), (i * MyDefine.CHARACTER_RESOLUTION[0],
                                                    j * MyDefine.CHARACTER_RESOLUTION[1],
                                                    MyDefine.CHARACTER_RESOLUTION[0],
                                                    MyDefine.CHARACTER_RESOLUTION[1]))
                self.m_frames[orientationName].append(frame_surface)

    def load_action_from_list(self, actionName, orientationName, frames):
        res = ImageManager.get_instance().find_resource_by_name(actionName)
        for i in range(len(frames)):
            frame_surface = pygame.Surface(MyDefine.CHARACTER_RESOLUTION)
            frame_surface.blit(res["image"], (0, 0), (frames[i][1] * MyDefine.CHARACTER_RESOLUTION[0],
                                                      frames[i][0] * MyDefine.CHARACTER_RESOLUTION[1],
                                                      MyDefine.CHARACTER_RESOLUTION[0],
                                                      MyDefine.CHARACTER_RESOLUTION[1]))
            self.m_frames[orientationName].append(frame_surface)

    def update(self):
        max_value = self.m_object.m_orientation.dot_product(ACTION_VECTORS[self.m_orientation])
        for i in range(len(ACTION_VECTORS)):
            dot_value = self.m_object.m_orientation.dot_product(ACTION_VECTORS[i])
            if dot_value >= max_value:
                max_value = dot_value
                self.m_orientation = i

        curSec = MyDefine.convert_nsec_to_msec(time.time_ns())
        if math.floor(BASIC_ACTION_FREQUENCY * (curSec - self.m_sec) / 1000) > 0:
            self.m_frame_index = (self.m_frame_index + 1) % len(self.m_frames[ACTION_ORIENTATION[self.m_orientation]])
            self.m_sec = curSec
        self.image = self.m_frames[ACTION_ORIENTATION[self.m_orientation]][self.m_frame_index]
        self.set_center_pos(self.m_object.m_position.x, self.m_object.m_position.z)

    def set_center_pos(self, x, z):
        if self.image:
            self.rect = self.image.get_rect()
            self.rect.center = (x, z)
