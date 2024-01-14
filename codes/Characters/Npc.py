from codes.Characters.Character import Character


class Npc(Character):

    def __init__(self, fsm_name):
        super().__init__(fsm_name)

    def update(self):
        super().update()
