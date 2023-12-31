import pygame
import pygame.image
import math
import time
from codes import MyDefine

# Direction of a character
MAX_CHARACTER_DIRECTION_COUNT = 4
# Basic move speed (m/s)
BASIC_CHARACTER_MOVE_SPEED = 0.5
# Basic action frequency of a character (frame/second)
BASIC_CHARACTER_ACTION_FREQUENCY = 4


class Character(pygame.sprite.Sprite):
    """Basic class of all characters"""

    def __init__(self, row, col, frameCount, resFile):
        """Constructive method"""
        super().__init__()

        # Initialize member-variables
        self.m_row = row
        self.m_col = col
        self.m_frameCount = frameCount
        self.m_resFile = resFile
        self.m_action = {'direction': 0, 'index': 0}  # (0:↓ 1:→ 2:↑ 3:←)
        self.rect = None
        self.m_milliseconds = MyDefine.convert_nsec_to_msec(time.time_ns())

        # Load resource
        self.resImage = pygame.image.load(self.m_resFile).convert()
        self.image = None

        # Counter-Clockwise Direction (↓ → ↑ ←)
        self.m_frames = []
        for i in range(MAX_CHARACTER_DIRECTION_COUNT):
            frames = []
            for j in range(self.m_frameCount):
                frame_surface = pygame.Surface(MyDefine.CHARACTER_RESOLUTION)
                frame_surface.blit(self.resImage, (0, 0), ((self.m_col + j) * MyDefine.CHARACTER_RESOLUTION[0],
                                                           (self.m_row + i) * MyDefine.CHARACTER_RESOLUTION[1],
                                                           MyDefine.CHARACTER_RESOLUTION[0],
                                                           MyDefine.CHARACTER_RESOLUTION[1]))
                frames.append(frame_surface)
            self.m_frames.append(frames)

    def update(self):
        """Update frame status"""
        curMillisecond = MyDefine.convert_nsec_to_msec(time.time_ns())
        if math.floor(BASIC_CHARACTER_ACTION_FREQUENCY * (curMillisecond - self.m_milliseconds) / 1000) > 0:
            self.m_action['index'] += 1
            self.m_milliseconds = curMillisecond

        self.m_action['index'] = (self.m_action['index']) % self.m_frameCount
        self.image = self.m_frames[self.m_action['direction']][self.m_action['index']]
        self.setCenterPos(400, 300)

    def setCenterPos(self, x, z):
        """Set center position of the character"""
        self.rect = self.image.get_rect()
        self.rect.center = (x, z)
