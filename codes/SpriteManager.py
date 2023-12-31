import pygame
from codes.Singelton import Singleton


class SpriteManager(Singleton):
    """Centralized management of all sprites"""

    def __init__(self):
        self.m_sprites = pygame.sprite.Group()

    def append_sprite(self, sprite):
        self.m_sprites.add(sprite)

    def update(self):
        self.m_sprites.update()

    def render(self, window):
        self.m_sprites.draw(window)
