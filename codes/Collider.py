from codes import MyDefine
from codes.Vector import Vector
from codes.BlockLayer import BlockLayer


class Collider:
    def __init__(self, action, pos, radius, obj):
        self.m_action = action
        self.m_relative_pos = pos
        self.m_radius = radius
        self.m_object = obj
        self.m_row = MyDefine.INVALID_ID
        self.m_col = MyDefine.INVALID_ID

    def update(self, x, z):
        blocks = BlockLayer.get_instance().m_blocks
        objects = BlockLayer.get_instance().m_objects

        pos = Vector(x, z) + self.m_relative_pos
        row = int(pos.z // MyDefine.BLOCK_RESOLUTION[0])
        col = int(pos.x // MyDefine.BLOCK_RESOLUTION[1])
        if self.m_row != row or self.m_col != col:
            if self.m_row != MyDefine.INVALID_ID and self.m_col != MyDefine.INVALID_ID:
                if blocks[self.m_row][self.m_col] == MyDefine.BLOCK_PLACEHOLDERS[2]:
                    blocks[self.m_row][self.m_col] = MyDefine.BLOCK_PLACEHOLDERS[0]
                    objects[f'{self.m_row},{self.m_col}'] = None
            self.m_row = row
            self.m_col = col
            if 0 <= self.m_row < len(blocks) and 0 <= self.m_col < len(blocks[self.m_row]):
                if blocks[self.m_row][self.m_col] == MyDefine.BLOCK_PLACEHOLDERS[0]:
                    blocks[self.m_row][self.m_col] = MyDefine.BLOCK_PLACEHOLDERS[2]
                    objects[f'{self.m_row},{self.m_col}'] = self.m_object
