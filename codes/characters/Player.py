import pygame
from codes.characters.Character import Character
from codes.EventTrigger import EventTrigger
from codes.EventTriggerManager import EventTriggerManager
from codes.Vector import Vector


class Player(Character, EventTrigger):

    def __init__(self, fsm_name):
        super().__init__(fsm_name)
        EventTriggerManager.get_instance().append_trigger(self)
        self.m_move_flag = False

    def update(self):
        super().update()

    def trigger(self, event):
        # Clicked on the right button
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pass

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            pass

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_pos = pygame.mouse.get_pos()
            self.move(Vector(mouse_pos[0], mouse_pos[1]))

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.onDamaged(-self.m_max_hp * 20 / 100)
            elif event.key == pygame.K_a:
                self.attack(None)
