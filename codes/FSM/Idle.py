import time
from codes import MyDefine
from codes.FSM.State import State

BLOOD_VOLUME_RESTORED_PER_SECOND = 3 / 100  # 每秒恢复的血量


class Idle(State):
    def __init__(self, obj):
        super().__init__(obj)
        self.m_sec = 0

    def begin(self, arg1):
        super().begin(arg1)
        # Action
        self.m_object.change_action(0)
        self.m_sec = MyDefine.convert_nsec_to_msec(time.time_ns())

    def update(self):
        super().update()

        current_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
        elapsed_sec = current_sec - self.m_sec
        self.m_sec = current_sec

        self.m_object.m_hp = min(self.m_object.m_max_hp, self.m_object.m_hp + self.m_object.m_max_hp *
                                 BLOOD_VOLUME_RESTORED_PER_SECOND * (elapsed_sec / 1000))

    def end(self):
        return super().end()
