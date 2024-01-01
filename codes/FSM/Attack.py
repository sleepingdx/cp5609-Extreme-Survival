from codes.FSM.State import State


class Attack(State):
    def __init__(self, obj):
        super().__init__(obj)
        self.m_object = obj

    def begin(self):
        super().begin()
        self.m_object.change_action(2)

    def run(self):
        super().run()
        pass

    def end(self):
        super().end()
