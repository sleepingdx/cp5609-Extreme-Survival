from codes.FSM.State import State


class Attack(State):
    def __init__(self, obj):
        super().__init__(obj)
        self.m_target = None

    def begin(self, target):
        super().begin(target)
        self.m_target = target
        self.m_target.onDamaged(self.m_target.m_max_hp * 10 / 100)
        self.m_object.change_action(2)

    def update(self):
        super().update()
        # Action has finished
        if self.m_object.is_action_completed(self.m_object.m_current):
            if not self.m_object.m_fsm.change_state(self.m_object.m_fsm.m_last_state):
                self.m_object.m_fsm.change_state(0, self.m_arg1)

    def end(self):
        return super().end()
