import pygame
import time
from codes import MyDefine
from codes.Character import Character
from codes.EventTrigger import EventTrigger
from codes.EventTriggerManager import EventTriggerManager
from codes.Vector import Vector


class Player(Character, EventTrigger):

    def __init__(self):
        super().__init__()
        EventTriggerManager.get_instance().append_trigger(self)

    def update(self):
        super().update()

    def trigger(self, event):
        # Clicked on the right button
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_pos = pygame.mouse.get_pos()
            self.m_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
            self.m_target_pos = Vector(mouse_pos[0], mouse_pos[1])
            self.move()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.onDamaged(-self.m_max_hp * 20 / 100)
            elif event.key == pygame.K_a:
                self.attack(None)
            elif event.key == pygame.K_UP:
                self.m_target_pos.x = self.m_position.x
                self.m_target_pos.z = self.m_position.z - 48
                self.move()
            elif event.key == pygame.K_DOWN:
                self.m_target_pos.x = self.m_position.x
                self.m_target_pos.z = self.m_position.z + 48
                self.move()
            elif event.key == pygame.K_LEFT:
                self.m_target_pos.x = self.m_position.x - 48
                self.m_target_pos.z = self.m_position.z
                self.move()
            elif event.key == pygame.K_RIGHT:
                self.m_target_pos.x = self.m_position.x + 48
                self.m_target_pos.z = self.m_position.z
                self.move()
