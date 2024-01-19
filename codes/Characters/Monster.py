from codes.Characters.Npc import Npc
from codes.DecisionTree.WarriorDT import WarriorDT


class Monster(Npc):

    def __init__(self, fsm_name):
        super().__init__(fsm_name)
        self.m_decision_tree = WarriorDT(self)

    def update(self):
        self.m_decision_tree.update()
        # Super
        super().update()
