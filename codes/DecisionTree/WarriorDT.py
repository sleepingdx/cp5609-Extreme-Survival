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
        # Find the nearest enemy
        blocks = BlockLayer.get_instance().m_blocks
        row_left = max(0, int((self.m_object.m_position.z - self.m_object.m_search_enemy_scope * MyDefine.MAP_GRID) //
                              MyDefine.BLOCK_RESOLUTION[0]))
        row_right = min(len(blocks) - 1,
                        int((self.m_object.m_position.z + self.m_object.m_search_enemy_scope * MyDefine.MAP_GRID) //
                            MyDefine.BLOCK_RESOLUTION[0]))
        col_top = max(0, int((self.m_object.m_position.x - self.m_object.m_search_enemy_scope * MyDefine.MAP_GRID) //
                             MyDefine.BLOCK_RESOLUTION[1]))
        col_bottom = min(len(blocks[row_left]) - 1,
                         int((self.m_object.m_position.x + self.m_object.m_search_enemy_scope * MyDefine.MAP_GRID) //
                             MyDefine.BLOCK_RESOLUTION[1]))
        final_distance = None
        target = None
        for row in range(row_left, row_right + 1):
            for col in range(col_top, col_bottom + 1):
                objects = BlockLayer.get_instance().m_objects[f'{row},{col}']
                for i in range(len(objects)):
                    if self.m_object != objects[i] and objects[i].m_hp > 0 and objects[i].m_type in TARGET_TYPES:
                        distance = (objects[i].m_position - self.m_object.m_position).calculate_magnitude2()
                        if not final_distance:
                            final_distance = distance
                        elif distance <= final_distance:
                            final_distance = distance
                        if distance <= (self.m_object.m_search_enemy_scope * MyDefine.MAP_GRID) ** 2:
                            target = objects[i]

        # Decision Tree
        if self.m_object.m_hp / self.m_object.m_max_hp < 50 / 100:
            if target:
                self.change_state(4, target)
            else:
                self.change_state(0, None)
        else:
            if target:
                if final_distance <= (self.m_object.m_attack_enemy_scope * MyDefine.MAP_GRID) ** 2:
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
