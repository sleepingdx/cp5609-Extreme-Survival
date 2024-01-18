from codes.FSM.State import State


class Attack(State):
    def __init__(self, obj):
        super().__init__(obj)
        self.m_target = None

    def begin(self, target):
        super().begin(target)
        self.m_target = target
        if self.m_target:
            self.m_object.change_action(2)
        else:
            self.m_object.m_fsm.change_state(0, None)

    def update(self):
        super().update()
        # Complete action
        if self.m_object.is_action_completed(self.m_object.m_current):
            # 如果不能在同一帧调用target object. 就做成队列
            self.m_target.onDamaged(self.m_target.m_max_hp * 2 / 100)
            if not self.m_object.m_fsm.change_state(self.m_object.m_fsm.m_last_state):
                self.m_object.m_fsm.change_state(0, self.m_arg1)

    def end(self):
        return super().end()
