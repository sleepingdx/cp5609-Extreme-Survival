from codes import MyDefine
from codes.BlockLayer import BlockLayer


class State:
    def __init__(self, obj):
        self.m_object = obj
        self.m_row = MyDefine.INVALID_ID
        self.m_col = MyDefine.INVALID_ID
        self.m_arg1 = None

    def begin(self, arg1):
        self.m_arg1 = arg1
        self.m_row = int(self.m_object.m_position.z // MyDefine.BLOCK_RESOLUTION[0])
        self.m_col = int(self.m_object.m_position.x // MyDefine.BLOCK_RESOLUTION[1])

    def update(self):
        # Calculate row & col
        row = int(self.m_object.m_position.z // MyDefine.BLOCK_RESOLUTION[0])
        col = int(self.m_object.m_position.x // MyDefine.BLOCK_RESOLUTION[1])
        if self.m_row != row or self.m_col != col:
            BlockLayer.get_instance().remove(self.m_row, self.m_col, self.m_object)
            self.m_row = row
            self.m_col = col
            BlockLayer.get_instance().append(self.m_row, self.m_col, self.m_object)

    def end(self):
        self.m_row = MyDefine.INVALID_ID
        self.m_col = MyDefine.INVALID_ID
        return self.m_arg1
