from codes.FSM.State import State


class Dead(State):
    def __init__(self, obj):
        super().__init__(obj)
        self.m_object = obj

    def begin(self):
        super().begin()
        self.m_object.change_action(3)

    def update(self):
        super().update()

    def end(self):
        super().end()
