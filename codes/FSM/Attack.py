from codes.FSM.State import State


class Attack(State):
    def __init__(self, obj):
        super().__init__(obj)

    def begin(self):
        super().begin()
        self.m_object.change_action(2)

    def update(self):
        super().update()
        # Action has finished
        if self.m_object.is_action_completed(self.m_object.m_current):
            self.m_object.m_fsm.change_status(0)

    def end(self):
        super().end()
