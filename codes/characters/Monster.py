from codes import MyDefine
from codes.characters.Npc import Npc

ENEMY_DETECTION_RANGE = 3 * MyDefine.MAP_GRID  # Scope of Searching enemies


class Monster(Npc):

    def __init__(self):
        super().__init__()

    def update(self):
        super().update()
