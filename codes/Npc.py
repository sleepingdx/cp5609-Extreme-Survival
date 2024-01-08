from codes.Character import Character


class Npc(Character):
    """"""

    def __init__(self):
        super().__init__()

    def update(self):
        super().update()
        self.m_fsm.update()
