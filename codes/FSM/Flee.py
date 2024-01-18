import math
import random
import time
from codes import MyDefine
from codes.FSM.State import State
from codes.BlockLayer import BlockLayer
from codes.PathFinding import PathFinding

BLOOD_VOLUME_RESTORED_PER_SECOND = 5 / 100  # 每秒恢复的血量


class Flee(State):
    def __init__(self, obj):
        super().__init__(obj)
        self.m_target = None
        self.m_path = []
        self.m_current = 0
        self.m_sec = 0

    def begin(self, target):
        super().begin(target)
        self.m_speed = MyDefine.BASIC_CHARACTER_FLEE_SPEED
        self.m_target = target
        if self.m_target:
            # Orientation
            orientation = (self.m_object.m_position - self.m_target.m_position).normalize()
            angle = math.radians(random.randint(-45, 45))
            orientation.x *= math.cos(angle)
            orientation.z *= math.sin(angle)
            for i in range(20, -10, -1):
                new_pos = self.m_object.m_position + orientation * MyDefine.MAP_GRID * i
                angle = math.radians(random.randint(0, 45))
                new_pos.x *= math.cos(angle)
                new_pos.z *= math.sin(angle)
                self.m_path = self.m_object.is_pos_arrived(new_pos)
                if len(self.m_path) > 0:
                    del self.m_path[0]
                self.m_current = 0
                break
            # # Path
            # blocks = BlockLayer.get_instance().m_blocks
            # self.m_path = PathFinding.astar_pos_ex(blocks, (self.m_object.m_position.x, self.m_object.m_position.z),
            #                                        (new_pos.x, new_pos.z))
            # if len(self.m_path) > 0:
            #     del self.m_path[0]
            # self.m_current = 0
            # Action
            self.m_object.change_action(1)
            self.m_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
        else:
            self.m_object.m_fsm.change_state(0)

    def update(self):
        super().update()
        # Time
        current_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
        elapsed_sec = current_sec - self.m_sec
        self.m_sec = current_sec

        self.m_object.m_hp = min(self.m_object.m_max_hp, self.m_object.m_hp + self.m_object.m_max_hp *
                                 BLOOD_VOLUME_RESTORED_PER_SECOND * (elapsed_sec / 1000))
        # Start to move
        if len(self.m_path) > 0:
            if self.m_object.find_path(self, self.m_speed, elapsed_sec):
                self.m_object.m_fsm.change_state(0)
        else:
            self.m_object.m_fsm.change_state(0)

    def end(self):
        self.m_target = None
        self.m_path.clear()
        self.m_current = 0
        return super().end()
