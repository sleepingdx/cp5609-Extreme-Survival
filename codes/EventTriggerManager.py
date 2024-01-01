import pygame
from codes.Singelton import Singleton


class EventTriggerManager(Singleton):
    def __init__(self):
        self.m_listeners = []

    def append_trigger(self, obj):
        if obj and obj not in self.m_listeners:
            self.m_listeners.append(obj)
            return True
        else:
            return False

    def remove_trigger(self, obj):
        if obj and obj in self.m_listeners:
            self.m_listeners.remove(obj)
            return True
        else:
            return False

    def trigger(self):
        for event in pygame.event.get():
            for i in range(len(self.m_listeners)):
                self.m_listeners[i].trigger(event)
