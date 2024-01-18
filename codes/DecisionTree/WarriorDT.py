from codes import MyDefine
from codes.BlockLayer import BlockLayer
from codes.DecisionTree.BasicDT import BasicDT

TARGET_TYPES = ("Player", "Npc", "Pet", "Monster")  # Type of attack target


class WarriorDT(BasicDT):
    def __init__(self, obj):
        super().__init__(obj)

    def begin(self):
        pass

    def update(self):
        super().update()
        if self.m_object.m_fsm.m_current in (0, 2):
            # Decision Tree
            if self.m_object.m_hp / self.m_object.m_max_hp < 70 / 100:
                target, _ = self.m_object.find_nearest_enemy()
                if target:
                    self.change_state(4, target)
                else:
                    self.change_state(0, None)
            else:
                target, distance2 = self.m_object.find_nearest_enemy()
                if target:
                    if distance2 <= (target.m_attack_enemy_scope * MyDefine.MAP_GRID) ** 2:
                        self.change_state(5, target)
                    else:
                        self.change_state(3, target)
                else:
                    if self.m_object.m_hp < self.m_object.m_max_hp:
                        self.change_state(0, None)
                    else:
                        self.change_state(2, None)

    def end(self):
        super().end()
        pass
