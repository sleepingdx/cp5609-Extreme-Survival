from codes.FSM.State import State


class Interact(State):
    def __init__(self, obj):
        super().__init__(obj)

    def begin(self, arg1):
        super().begin(arg1)
        self.m_object.change_action(0)

    def update(self):
        super().update()

    def end(self):
        return super().end()
