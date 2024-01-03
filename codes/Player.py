import pygame
import time
from codes import MyDefine
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
        self.m_target_pos = Vector(0, 0)
        self.m_sec = MyDefine.convert_nsec_to_msec(time.time_ns())

    def update(self):
        super().update()
        self.m_fsm.update()

    def trigger(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            self.m_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
            self.m_target_pos = Vector(mouse_pos[0], mouse_pos[1])
            self.m_fsm.change_status(1)
