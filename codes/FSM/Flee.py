import time
from codes import MyDefine
from codes.FSM.State import State
from codes.BlockLayer import BlockLayer
from codes.PathFinding import PathFinding


class Flee(State):
    def __init__(self, obj):
        super().__init__(obj)
        self.m_target = None
        self.m_path = []
        self.m_current = 0
        self.m_sec = 0

    def begin(self, obj):
        super().begin(obj)
        self.m_target = obj
        if self.m_target:
            target_pos = self.m_target.m_position
            # Path
            blocks = BlockLayer.get_instance().m_blocks
            row = min(max(0, int(target_pos.z // MyDefine.BLOCK_RESOLUTION[0])), len(blocks) - 1)
            col = min(max(0, int(target_pos.x // MyDefine.BLOCK_RESOLUTION[1])), len(blocks[row]) - 1)
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
        else:
            self.m_object.m_fsm.change_state(0)

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
                       * MyDefine.BASIC_CHARACTER_FLEE_SPEED * (elapsed_sec / 1000))

            if self.m_object.find_path(self, new_pos):
                self.m_object.m_fsm.change_state(0)
        else:
            self.m_object.m_fsm.change_state(0)

    def end(self):
        self.m_target = None
        self.m_path.clear()
        self.m_current = 0
        return super().end()
