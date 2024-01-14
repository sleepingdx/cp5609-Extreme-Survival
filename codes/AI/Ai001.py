import random
import time

from codes import MyDefine
from codes.AI.BaseAI import BaseAI

SEARCH_ENEMY_RADIUS = 5 * MyDefine.MAP_GRID  # Radius of searching enemies
PATROL_TIME = (3000, 8000)  # The range of random seconds(ms) of patrolling


class Ai001(BaseAI):
    def __init__(self, obj):
        super().__init__(obj)
        self.m_patrol_cd = PATROL_TIME[0]

    def begin(self):
        super().begin()

    def update(self, msec):
        super().update(msec)
        # Patrolling
        if self.m_object.m_fsm.m_current == 0:
            if self.m_patrol_cd <= 0:
                self.m_patrol_cd = random.randint(PATROL_TIME[0], PATROL_TIME[1])
                self.m_object.patrol()
            else:
                self.m_patrol_cd -= msec

    def end(self):
        super().end()
