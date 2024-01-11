from codes.FSM.State import State


class Injured(State):
    def __init__(self, obj):
        super().__init__(obj)

    def begin(self):
        super().begin()
        self.m_object.change_action(3)

    def update(self):
        super().update()
        # Action has finished
        if self.m_object.is_action_completed(self.m_object.m_current):
            if self.m_object.m_hp <= 0:
                self.m_object.onDied()
            elif self.m_object.m_fsm.m_last_state != 3:
                self.m_object.m_fsm.change_status(self.m_object.m_fsm.m_last_state)

    def end(self):
        super().end()
