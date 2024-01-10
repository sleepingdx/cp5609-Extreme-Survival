from codes import MyDefine
from codes.BlockLayer import BlockLayer


class State:
    def __init__(self, obj):
        self.m_object = obj
        self.m_row = MyDefine.INVALID_ID
        self.m_col = MyDefine.INVALID_ID

    def begin(self):
        pass

    def update(self):
        row = int(self.m_object.m_position.z // MyDefine.BLOCK_RESOLUTION[0])
        col = int(self.m_object.m_position.x // MyDefine.BLOCK_RESOLUTION[1])
        blocks = BlockLayer.get_instance().m_blocks
        if self.m_row != row or self.m_col != col:
            # BlockLayer.get_instance().remove(self.m_row, self.m_col, self.m_object, MyDefine.BLOCK_PLACEHOLDERS[0])
            self.m_row = row
            self.m_col = col
            if 0 <= self.m_row < len(blocks) and 0 <= self.m_col < len(blocks[self.m_row]):
                BlockLayer.get_instance().append(self.m_row, self.m_col, self.m_object, MyDefine.BLOCK_PLACEHOLDERS[2])

    def end(self):
        pass
