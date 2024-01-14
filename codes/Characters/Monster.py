from codes import MyDefine
from codes.Characters.Npc import Npc

ENEMY_DETECTION_RANGE = 3 * MyDefine.MAP_GRID  # Scope of Searching enemies


class Monster(Npc):

    def __init__(self, fsm_name):
        super().__init__(fsm_name)

    def update(self):
        super().update()
