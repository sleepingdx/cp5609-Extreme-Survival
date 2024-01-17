from codes.Characters.Npc import Npc


class Pet(Npc):

    def __init__(self, fsm_name):
        super().__init__(fsm_name)

    def update(self):
        super().update()

    def render(self, window):
        super().render(window)
        self.draw_health_bar(window)

