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
        # Generate a random position
        self.m_radius = random.randint(PATROL_RANDOM_RADIUS_RANGE[0], PATROL_RANDOM_RADIUS_RANGE[1])
        angle = math.radians(random.randint(0, 360))
        x = self.m_object.m_position.x + random.randint(1, self.m_radius) * math.cos(angle)
        z = self.m_object.m_position.z + random.randint(1, self.m_radius) * math.sin(angle)
        # Path
        blocks = BlockLayer.get_instance().m_blocks
        row = min(max(0, int(z // MyDefine.BLOCK_RESOLUTION[0])), len(blocks) - 1)
        col = min(max(0, int(x // MyDefine.BLOCK_RESOLUTION[1])), len(blocks[row]) - 1)
        if blocks[row][col] != MyDefine.BLOCK_PLACEHOLDERS[0]:
            directions = ((row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1),
                          (row + 1, col - 1), (row + 1, col), (row + 1, col + 1))
            for i in range(len(directions)):
                if 0 <= directions[i][0] < len(blocks) and 0 <= directions[i][1] < len(blocks[directions[i][0]]):
                    if blocks[directions[i][0]][directions[i][1]] == MyDefine.BLOCK_PLACEHOLDERS[0]:
                        row = directions[i][0]
                        col = directions[i][1]
                        break
        self.m_path = PathFinding.astar_pos(blocks, (self.m_row, self.m_col), (row, col))
        if len(self.m_path) > 0:
            del self.m_path[0]
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
            # Velocity
            orientation = (self.m_path[self.m_current] - self.m_object.m_position).normalize()
            new_pos = (self.m_object.m_position + orientation * MyDefine.PIXELS_PER_METER
                       * MyDefine.BASIC_CHARACTER_MOVE_SPEED * (elapsed_sec / 1000))

            if self.m_object.path_finding(self, new_pos):
                self.m_object.m_fsm.change_state(0)
        else:
            self.m_object.m_fsm.change_state(0)

    def end(self):
        self.m_path.clear()
        self.m_current = 0
        return super().end()
