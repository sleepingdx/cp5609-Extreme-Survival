import pygame
import pygame.image
import math
import time
from codes import MyDefine
from codes.ImageManager import ImageManager
from codes.Vector import Vector

BASIC_EFFECT_FREQUENCY = 5  # Basic action frequency (f/s)


class Effect(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        self.m_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
        self.m_frames = []
        self.m_frame_index = 0
        self.image = None
        self.rect = None
        self.m_completed = False
        self.m_position = Vector(0, 0)
        # 因为不是一次性加在全部资源， 所以每次使用前需要确认该资源已经被加载了
        if filename != '':
            ImageManager.get_instance().load_resource(filename, filename)
        self.m_filename = filename

    def load_frames(self, frames, resolution):
        if self.m_filename == '':
            return
        res = ImageManager.get_instance().find_resource_by_name(self.m_filename)
        for i in range(len(frames)):
            frame_surface = pygame.Surface(resolution, pygame.SRCALPHA)
            frame_surface.blit(res["image"], (0, 0), (
                frames[i][1] * resolution[0], frames[i][0] * resolution[1], resolution[0], resolution[1]))
            self.m_frames.append(frame_surface)

    def update(self):
        if self.m_filename == '':
            return
        curSec = MyDefine.convert_nsec_to_msec(time.time_ns())
        if math.floor(BASIC_EFFECT_FREQUENCY * (curSec - self.m_sec) / 1000) > 0:
            self.m_frame_index = (self.m_frame_index + 1) % len(self.m_frames)
            self.m_sec = curSec
            if self.m_frame_index == 0:
                self.m_completed = True
        self.image = self.m_frames[self.m_frame_index]
        self.set_center_pos(self.m_position.x, self.m_position.z)

    def set_center_pos(self, x, z):
        if self.m_filename == '':
            return
        self.m_position = Vector(x, z)
        if self.image:
            self.rect = self.image.get_rect()
            self.rect.center = (x, z)
