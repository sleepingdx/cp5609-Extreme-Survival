import time
from codes import MyDefine
from codes.FSM.State import State
from codes.BlockLayer import BlockLayer
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

        orientation = (self.m_object.m_target_pos - self.m_object.m_position)
        if orientation.calculate_magnitude2() <= MyDefine.ARRIVE_TARGET_POS_RANGE ** 2:
            self.m_object.m_fsm.change_status(0)
            return
        else:
            orientation.normalize()
            self.m_object.m_orientation = orientation
            new_pos = (self.m_object.m_position + orientation * MyDefine.PIXELS_PER_METER *
                       MyDefine.BASIC_CHARACTER_MOVE_SPEED * (elapsed_sec / 1000))
            # Collision Detection
            blocks = BlockLayer.get_instance().m_blocks
            objects = BlockLayer.get_instance().m_objects
            for r in range(self.m_row - 1, self.m_row + 1):
                for c in range(self.m_col - 1, self.m_col + 1):
                    if blocks[r][c] == MyDefine.BLOCK_PLACEHOLDERS[1]:
                        center_pos = Vector(
                            c * MyDefine.BLOCK_RESOLUTION[0] + MyDefine.BLOCK_PLACEHOLDERS[0] / 2,
                            r * MyDefine.BLOCK_PLACEHOLDERS[1] + MyDefine.BLOCK_RESOLUTION[1] / 2)
                        distance = (center_pos - new_pos).calculate_magnitude2()
                        if distance < (
                                self.m_object.get_rect().width / 2 + MyDefine.BLOCK_RESOLUTION[0] / 2) ** 2:
                            self.m_object.m_fsm.change_status(0)
                            return
                    elif blocks[r][c] == MyDefine.BLOCK_PLACEHOLDERS[2]:
                        for i in range(len(objects[f'{r},{c}'])):
                            if objects[f'{r},{c}'][i] and objects[f'{r},{c}'][i] != self.m_object:
                                distance = (objects[f'{r},{c}'][i].m_position - new_pos).calculate_magnitude2()
                                if distance < (
                                        objects[f'{r},{c}'][
                                            i].get_rect().width / 2 + self.m_object.get_rect().width / 2) ** 2:
                                    self.m_object.m_fsm.change_status(0)
                                    return
                    else:
                        pass
            self.m_object.m_position = new_pos

    def end(self):
        super().end()
