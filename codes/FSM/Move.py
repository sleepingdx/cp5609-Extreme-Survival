import time
from codes import MyDefine
from codes.FSM.State import State
from codes.Vector import Vector


class Move(State):
    def __init__(self, obj):
        super().__init__(obj)
        self.m_object = obj

    def begin(self):
        super().begin()
        self.m_object.change_action(1)

    def update(self):
        super().update()
        current_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
        elapsed_sec = current_sec - self.m_object.m_sec
        self.m_object.m_sec = current_sec

        vector = (self.m_object.m_target_pos - self.m_object.m_position)
        if vector.calculate_magnitude2() <= MyDefine.ARRIVE_TARGET_POS_RANGE ** 2:
            self.m_object.m_fsm.change_status(0)
            return
        else:
            vector.normalize()
            self.m_object.m_orientation = vector
            self.m_object.m_position += vector * MyDefine.PIXELS_PER_METER * MyDefine.BASIC_CHARACTER_MOVE_SPEED * (
                    elapsed_sec / 1000)

    def end(self):
        super().end()
