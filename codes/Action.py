import pygame
import pygame.image
import math
import time
from codes import MyDefine
from codes.ImageManager import ImageManager
from codes.Vector import Vector

BASIC_ACTION_FREQUENCY = 6  # Basic action frequency (f/s)
ACTION_ORIENTATION = ["Up", "Right", "Down", "Left"]
ACTION_VECTORS = [Vector(0, -1), Vector(1, 0), Vector(0, 1), Vector(-1, 0)]


class Action(pygame.sprite.Sprite):
    """Subclass of Sprite"""

    def __init__(self, obj, filename):
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
        self.m_colliders = []
        self.image = None
        self.rect = None
        self.m_completed = False
        self.m_effect = None
        # 因为不是一次性加在全部资源， 所以每次使用前需要确认该资源已经被加载了
        if filename != '':
            ImageManager.get_instance().load_resource(filename, filename)
        self.m_filename = filename

    def load_action_by_index(self, orientationName, beginRow, beginCol, endRow, endCol, resolution):
        res = ImageManager.get_instance().find_resource_by_name(self.m_filename)
        for i in range(endRow - beginRow):
            for j in range(endCol - beginCol):
                frame_surface = pygame.Surface(resolution)
                frame_surface.blit(res[1], (0, 0), (i * resolution[0], j * resolution[1], resolution[0], resolution[1]))
                self.m_frames[orientationName].append(frame_surface)

    def load_action_from_list(self, orientationName, frames, resolution):
        res = ImageManager.get_instance().find_resource_by_name(self.m_filename)
        for i in range(len(frames)):
            frame_surface = pygame.Surface(resolution, pygame.SRCALPHA)
            frame_surface.blit(res["image"], (0, 0), (
                frames[i][1] * resolution[0], frames[i][0] * resolution[1], resolution[0], resolution[1]))
            self.m_frames[orientationName].append(frame_surface)

    def update(self):
        max_dot_value = self.m_object.m_orientation.dot_product(ACTION_VECTORS[self.m_orientation])
        for i in range(len(ACTION_VECTORS)):
            dot_value = self.m_object.m_orientation.dot_product(ACTION_VECTORS[i])
            if dot_value > max_dot_value:
                max_dot_value = dot_value
                self.m_orientation = i

        curSec = MyDefine.convert_nsec_to_msec(time.time_ns())
        if math.floor(BASIC_ACTION_FREQUENCY * (curSec - self.m_sec) / 1000) > 0:
            self.m_frame_index = (self.m_frame_index + 1) % len(
                self.m_frames[ACTION_ORIENTATION[self.m_orientation]])
            self.m_sec = curSec
            if self.m_frame_index == 0:
                self.m_completed = True
        self.image = self.m_frames[ACTION_ORIENTATION[self.m_orientation]][self.m_frame_index]
        self.set_center_pos(self.m_object.m_position.x, self.m_object.m_position.z)

    def set_center_pos(self, x, z):
        if self.image:
            self.rect = self.image.get_rect()
            self.rect.center = (x, z)
