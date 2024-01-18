import random
import time
from codes import MyDefine
from codes.FSM.State import State
from codes.BlockLayer import BlockLayer
from codes.PathFinding import PathFinding
from codes.Vector import Vector


class Flee(State):
    def __init__(self, obj):
        super().__init__(obj)
        self.m_target = None
        self.m_path = []
        self.m_current = 0
        self.m_sec = 0

    def begin(self, target):
        super().begin(target)
        self.m_target = target
        if self.m_target:
            # Orientation
            orientation = (self.m_object.m_position - self.m_target.m_position).normalize()
            new_pos = self.m_object.m_position + orientation * MyDefine.MAP_GRID
            # Path
            blocks = BlockLayer.get_instance().m_blocks
            self.m_path = PathFinding.astar_pos_ex(blocks, (self.m_object.m_position.x, self.m_object.m_position.z),
                                                   (new_pos.x, new_pos.z))
            if len(self.m_path) > 0:
                del self.m_path[0]
            sum = Vector(0, 0)
            num = len(self.m_path)
            for i in range(num):
                sum += self.m_path[i]
            distance = ((sum / num) - self.m_object.m_position).calculate_magnitude2()
            if distance <= MyDefine.ARRIVE_TARGET_POS_SCOPE ** 2:
                new_pos = (
                    random.randint(0, MyDefine.GAME_RESOLUTION[0]), random.randint(0, MyDefine.GAME_RESOLUTION[1]))
                self.m_path = PathFinding.astar_pos_ex(blocks, (self.m_object.m_position.x, self.m_object.m_position.z),
                                                       (new_pos[0], new_pos[1]))
            if len(self.m_path) > 0:
                del self.m_path[0]
            self.m_current = 0
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
        # Start to move
        if len(self.m_path) > 0:
            if self.m_object.find_path(self, MyDefine.BASIC_CHARACTER_FLEE_SPEED, elapsed_sec):
                self.m_object.m_fsm.change_state(0)
        else:
            self.m_object.m_fsm.change_state(0)

    def end(self):
        self.m_target = None
        self.m_path.clear()
        self.m_current = 0
        return super().end()
