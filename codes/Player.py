import pygame
from codes.Character import Character
from codes.EventTrigger import EventTrigger
from codes.EventTriggerManager import EventTriggerManager
from codes.Vector import Vector
from codes.FSM.FiniteStateMachine import FiniteStateMachine


class Player(Character, EventTrigger):

    def __init__(self):
        super().__init__()
        EventTriggerManager.get_instance().append_trigger(self)
        # FSM
        self.m_fsm = FiniteStateMachine(self, "Player")

    def update(self):
        super().update()

    def trigger(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            self.m_position = Vector(mouse_pos[0], mouse_pos[1])
