import time
from codes import MyDefine
from codes.Characters.Npc import Npc
from codes.AI.Ai001 import Ai001


class Monster(Npc):

    def __init__(self, fsm_name):
        super().__init__(fsm_name)
        self.m_ai_script = Ai001(self)
        self.m_ai_script.begin()
        self.m_sec = MyDefine.convert_nsec_to_msec(time.time_ns())

    def update(self):
        # Time
        current_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
        elapsed_sec = current_sec - self.m_sec
        self.m_sec = current_sec
        # AI
        self.m_ai_script.update(elapsed_sec)
        # Super
        super().update()

    def render(self, window):
        super().render(window)
        self.draw_health_bar(window)
