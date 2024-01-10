import time
from codes import MyDefine
from codes.FSM.State import State
from codes.BlockLayer import BlockLayer
from codes.Vector import Vector
from codes.CollisionDection import CollisionDetection


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
            for r in range(max(0, self.m_row - 1), min(self.m_row + 1 + 1, len(blocks))):
                for c in range(max(0, self.m_col - 1), min(self.m_col + 1 + 1, len(blocks[r]))):
                    if blocks[r][c] == MyDefine.BLOCK_PLACEHOLDERS[1]:
                        center_pos = Vector(
                            c * MyDefine.BLOCK_RESOLUTION[0] + MyDefine.BLOCK_RESOLUTION[0] / MyDefine.COLLIDER_RADIUS,
                            r * MyDefine.BLOCK_RESOLUTION[1] + MyDefine.BLOCK_RESOLUTION[1] / MyDefine.COLLIDER_RADIUS)
                        # if CollisionDetection.detect_circle_collision(
                        #         (center_pos.x, center_pos.z, MyDefine.BLOCK_RESOLUTION[0] / MyDefine.COLLIDER_RADIUS),
                        #         (new_pos.x, new_pos.z, MyDefine.BLOCK_RESOLUTION[0] / MyDefine.COLLIDER_RADIUS)):
                        #     self.m_object.m_fsm.change_status(0)
                        #     return
                        if CollisionDetection.detect_block_collision(
                                (center_pos.x, center_pos.z, MyDefine.BLOCK_COLLIDER_RANGE[0],
                                 MyDefine.BLOCK_COLLIDER_RANGE[1]),
                                (new_pos.x, new_pos.z, MyDefine.BLOCK_COLLIDER_RANGE[0],
                                 MyDefine.BLOCK_COLLIDER_RANGE[1])):
                            self.m_object.m_fsm.change_status(0)
                            return
                    elif blocks[r][c] == MyDefine.BLOCK_PLACEHOLDERS[2]:
                        objects = BlockLayer.get_instance().m_objects[f'{r},{c}']
                        if objects:
                            for i in range(len(objects)):
                                if objects[i] and objects[i] != self.m_object:
                                    # if CollisionDetection.detect_circle_collision(
                                    #         (objects[i].m_position.x, objects[i].m_position.z,
                                    #          MyDefine.BLOCK_RESOLUTION[0] / MyDefine.COLLIDER_RADIUS),
                                    #         (new_pos.x, new_pos.z,
                                    #          MyDefine.BLOCK_RESOLUTION[0] / MyDefine.COLLIDER_RADIUS)):
                                    if CollisionDetection.detect_block_collision(
                                            (objects[i].m_position.x, objects[i].m_position.z,
                                             MyDefine.BLOCK_COLLIDER_RANGE[0],
                                             MyDefine.BLOCK_COLLIDER_RANGE[1]),
                                            (new_pos.x, new_pos.z, MyDefine.BLOCK_COLLIDER_RANGE[0],
                                             MyDefine.BLOCK_COLLIDER_RANGE[1])):
                                        self.m_object.m_fsm.change_status(0)
                                        return
            self.m_object.m_position = new_pos

    def end(self):
        super().end()
