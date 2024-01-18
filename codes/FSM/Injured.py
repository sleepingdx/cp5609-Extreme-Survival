from codes.FSM.State import State


class Injured(State):
    def __init__(self, obj):
        super().__init__(obj)
        self.m_arg1 = None

    def begin(self, arg1):
        super().begin(arg1)
        self.m_arg1 = arg1
        self.m_object.change_action(3)

    def update(self):
        super().update()
        # Action has finished
        if self.m_object.m_hp <= 0:
            self.m_object.onDied()
        else:
            if not self.m_object.m_fsm.change_state(self.m_object.m_fsm.m_last_state):
                self.m_object.m_fsm.change_state(0, self.m_arg1)

    def end(self):
        return super().end()
