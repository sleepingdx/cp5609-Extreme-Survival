import time
from codes import MyDefine
from codes.FSM.State import State
from codes.BlockLayer import BlockLayer
from codes.PathFinding import PathFinding


class Chase(State):
    def __init__(self, obj):
        super().__init__(obj)
        self.m_target = None
        self.m_path = []
        self.m_current = 0
        self.m_sec = 0
        self.m_time = 0

    def begin(self, target):
        super().begin(target)
        self.m_target = target
        if self.m_target:
            self.m_speed = MyDefine.BASIC_CHARACTER_CHASE_SPEED
            distance = (self.m_target.m_position - self.m_object.m_position).calculate_magnitude()
            self.m_time = distance / (self.m_speed * MyDefine.PIXELS_PER_METER)
            # Action
            self.m_object.change_action(1)
            self.m_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
        else:
            self.m_object.m_fsm.change_state(0)

    def update(self):
        super().update()

        # Velocity
        current_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
        elapsed_sec = current_sec - self.m_sec
        self.m_sec = current_sec

        target_pos = self.m_target.m_position
        orientation = self.m_target.m_orientation
        speed = self.m_target.get_current_speed()
        predict_pos = target_pos + orientation * MyDefine.PIXELS_PER_METER * speed * MyDefine.PIXELS_PER_METER * (
                elapsed_sec / 1000)

        distance2 = (predict_pos - self.m_object.m_position).calculate_magnitude2()
        if distance2 <= (self.m_object.m_attack_enemy_scope * MyDefine.MAP_GRID) ** 2:
            self.m_object.m_fsm.change_state(2)
            return

            # Path
        blocks = BlockLayer.get_instance().m_blocks
        self.m_path = PathFinding.astar_pos_ex(blocks, (self.m_object.m_position.x, self.m_object.m_position.z),
                                               (predict_pos.x, predict_pos.z), True)
        if len(self.m_path) >= 2:
            del self.m_path[0]
            del self.m_path[-1]
        self.m_current = 0

        if len(self.m_path) > 0:
            # Calculate final speed
            self.m_speed = MyDefine.BASIC_CHARACTER_CHASE_SPEED
            if ((self.m_target.m_position - self.m_object.m_position).calculate_magnitude2() <=
                    MyDefine.DECELERATION_SCOPE ** 2):
                self.m_speed *= MyDefine.DECELERATION_RATE
            # Start to move
            if self.m_object.find_path(self, self.m_speed, elapsed_sec):
                self.m_path = PathFinding.astar_pos_ex(blocks, (self.m_object.m_position.x, self.m_object.m_position.z),
                                                       (predict_pos.x, predict_pos.z), True)
                # self.m_object.m_fsm.change_state(0)
        else:
            self.m_object.m_fsm.change_state(0)

    def end(self):
        self.m_target = None
        self.m_path.clear()
        self.m_current = 0
        return super().end()
