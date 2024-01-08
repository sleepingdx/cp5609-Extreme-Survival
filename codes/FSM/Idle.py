from codes import MyDefine
from codes.FSM.State import State
from codes.BlockLayer import BlockLayer


class Idle(State):
    def __init__(self, obj):
        super().__init__(obj)
        self.m_object = obj

    def begin(self):
        super().begin()
        self.m_object.change_action(0)

    def update(self):
        super().update()

    def end(self):
        super().end()
