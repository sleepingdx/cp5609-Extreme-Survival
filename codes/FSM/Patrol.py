import math
import time
import random
from codes import MyDefine
from codes.FSM.State import State
from codes.BlockLayer import BlockLayer
from codes.PathFinding import PathFinding

PATROL_RANDOM_RADIUS_RANGE = (5 * MyDefine.MAP_GRID, 10 * MyDefine.MAP_GRID)  # Radius scope


class Patrol(State):
    def __init__(self, obj):
        super().__init__(obj)
        self.m_radius = PATROL_RANDOM_RADIUS_RANGE[0]
        self.m_path = []
        self.m_current = 0
        self.m_sec = 0

    def begin(self, arg1):
        super().begin(arg1)
        self.m_speed = MyDefine.BASIC_CHARACTER_PATROL_SPEED
        # Generate a random position
        self.m_radius = random.randint(PATROL_RANDOM_RADIUS_RANGE[0], PATROL_RANDOM_RADIUS_RANGE[1])
        angle = math.radians(random.randint(0, 360))
        x = self.m_object.m_position.x + random.randint(1, self.m_radius) * math.cos(angle)
        z = self.m_object.m_position.z + random.randint(1, self.m_radius) * math.sin(angle)
        # Path
        blocks = BlockLayer.get_instance().m_blocks
        self.m_path = PathFinding.astar_pos_ex(blocks, (self.m_object.m_position.x, self.m_object.m_position.z), (x, z))
        self.m_current = 0
        # Action
        self.m_object.change_action(1)
        self.m_sec = MyDefine.convert_nsec_to_msec(time.time_ns())

    def update(self):
        super().update()
        if len(self.m_path) > 0:
            # Velocity
            current_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
            elapsed_sec = current_sec - self.m_sec
            self.m_sec = current_sec
            # Start to move
            if self.m_object.find_path(self, self.m_speed, elapsed_sec):
                self.m_object.m_fsm.change_state(0)
        else:
            self.m_object.m_fsm.change_state(0)

    def end(self):
        self.m_path.clear()
        self.m_current = 0
        return super().end()
