import pygame


class SpriteManager:
    """Centralized management of all sprites"""

    def __init__(self):
        self.m_sprites = pygame.sprite.Group()

    def append_sprite(self, sprite):
        self.m_sprites.add(sprite)

    def delete_sprite(self, sprite):
        self.m_sprites.remove(sprite)

    def update(self):
        self.m_sprites.update()

    def render(self, window):
        self.m_sprites.draw(window)
