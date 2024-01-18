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
        self.m_distances = {}
        self.m_sec = 0

    def begin(self, target):
        super().begin(target)
        self.m_speed = MyDefine.BASIC_CHARACTER_FLEE_SPEED
        self.m_target = target
        if self.m_target:
            blocks = BlockLayer.get_instance().m_blocks
            self.m_distances = PathFinding.dijkstra_ex(blocks, (self.m_target.m_position.x, self.m_target.m_position.z))
            if len(self.m_distances) > 0:
                # Assuming distances is a dictionary with keys as node coordinates and values as distances
                non_infinity_distances = {node: distance for node, distance in self.m_distances.items() if
                                          distance != float('infinity')}
                # Assuming distances is a dictionary with keys as node coordinates and values as distances
                sorted_distances = sorted(non_infinity_distances.items(), key=lambda x: x[1], reverse=True)
                # First element of sorted_distances is the node with the maximum distance
                max_distance_node, max_distance = sorted_distances[random.randint(0, 3)]
                # Extracting row and col from the node coordinates
                max_distance_row, max_distance_col = max_distance_node
                # Path
                self.m_path = PathFinding.astar_pos(blocks, (self.m_row, self.m_col),
                                                    (max_distance_row, max_distance_col))
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
        # Restore HP
        self.m_object.m_hp = min(self.m_object.m_max_hp, self.m_object.m_hp + self.m_object.m_max_hp *
                                 BLOOD_VOLUME_RESTORED_PER_SECOND * (elapsed_sec / 1000))
        if self.m_object.m_hp >= self.m_object.m_max_hp:
            self.m_object.m_fsm.change_state(2, None)
            return
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
