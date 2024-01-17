class BasicDT:
    def __init__(self, obj):
        self.m_object = obj

    def begin(self):
        pass

    def update(self):
        pass

    def end(self):
        pass

    def change_state(self, index, arg1):
        if self.m_object.m_fsm.m_current != index:
            self.m_object.m_fsm.change_state(index, arg1)
