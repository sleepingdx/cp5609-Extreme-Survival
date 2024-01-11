from codes import MyDefine
from codes.BlockLayer import BlockLayer


class State:
    def __init__(self, obj):
        self.m_object = obj

    def begin(self):
        pass

    def update(self):
        row = int(self.m_object.m_position.z // MyDefine.BLOCK_RESOLUTION[0])
        col = int(self.m_object.m_position.x // MyDefine.BLOCK_RESOLUTION[1])
        # blocks = BlockLayer.get_instance().m_blocks
        # objects = BlockLayer.get_instance().m_objects
        if self.m_object.m_row != row or self.m_object.m_col != col:
            BlockLayer.get_instance().remove(self.m_object.m_row, self.m_object.m_col, self.m_object)
            self.m_object.m_row = row
            self.m_object.m_col = col
            BlockLayer.get_instance().append(self.m_object.m_row, self.m_object.m_col, self.m_object)

    def end(self):
        pass
