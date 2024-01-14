from codes import MyDefine
from codes.characters.Character import Character

ENEMY_DETECTION_RANGE = 3 * MyDefine.MAP_GRID  # Scope of Searching enemies


class Npc(Character):

    def __init__(self):
        super().__init__()

    def update(self):
        super().update()
