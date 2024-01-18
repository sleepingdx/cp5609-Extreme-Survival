import time
from codes import MyDefine
from codes.FSM.State import State

DAMAGE_CD = 800


class Attack(State):
    def __init__(self, obj):
        super().__init__(obj)
        self.m_target = None
        self.m_sec = 0
        self.m_cd = DAMAGE_CD

    def begin(self, target):
        super().begin(target)
        self.m_target = target
        if self.m_target and self.m_target.m_hp > 0:
            self.m_cd = DAMAGE_CD
            # Action
            self.m_object.change_action(2)
            self.m_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
        else:
            self.m_object.m_fsm.change_state(0, None)

    def update(self):
        super().update()

        # Velocity
        current_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
        elapsed_sec = current_sec - self.m_sec
        self.m_sec = current_sec
        self.m_cd -= elapsed_sec
        if self.m_cd <= 0:
            self.m_cd = DAMAGE_CD
            # Calculate damage
            from codes.Characters.Character import Character
            damage = self.m_target.m_max_hp * 5 / 100
            self.m_target.push_event((Character.CHARACTER_EVENTS[1], damage))
        # Distance
        distance = (self.m_target.m_position - self.m_object.m_position).calculate_magnitude2()
        if distance > (self.m_object.m_attack_enemy_scope * MyDefine.MAP_GRID) ** 2 or self.m_target.m_hp <= 0:
            self.m_object.m_fsm.change_state(2, None)

    def end(self):
        return super().end()
