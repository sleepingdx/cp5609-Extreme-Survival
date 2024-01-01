import pygame
from codes.Character import Character
from codes.EventTrigger import EventTrigger
from codes.EventTriggerManager import EventTriggerManager


class Player(Character, EventTrigger):
    """"""

    def __init__(self):
        super().__init__()
        EventTriggerManager.get_instance().append_trigger(self)

    def update(self):
        super().update()

    def trigger(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            self.m_x = mouse_pos[0]
            self.m_z = mouse_pos[1]
