from codes import MyDefine


class Collider:
    def __init__(self, pos, radius, obj, block_layer):
        self.m_position = pos
        self.m_radius = radius
        self.m_object = obj
        self.m_block_layer = block_layer
        self.m_row = MyDefine.INVALID_ID
        self.m_col = MyDefine.INVALID_ID

    def update(self):
        pos = self.m_object.m_position
        row = pos.z % MyDefine.BLOCK_RESOLUTION[0]
        col = pos.x % MyDefine.BLOCK_RESOLUTION[1]
        if self.m_row != row or self.m_col != col:
            if self.m_row != MyDefine.INVALID_ID and self.m_col != MyDefine.INVALID_ID:
                if self.m_block_layer.m_blocks[self.m_row][self.m_col] == MyDefine.BLOCK_PLACEHOLDERS[2]:
                    self.m_block_layer.m_blocks[self.m_row][self.m_col] = MyDefine.BLOCK_PLACEHOLDERS[0]
                    self.m_block_layer.m_objects[f'{self.m_row},{self.m_col}'] = None
            self.m_row = row
            self.m_col = col
            if self.m_block_layer.m_blocks[self.m_row][self.m_col] == MyDefine.BLOCK_PLACEHOLDERS[0]:
                self.m_block_layer.m_blocks[self.m_row][self.m_col] = MyDefine.BLOCK_PLACEHOLDERS[2]
                self.m_block_layer.m_objects[f'{self.m_row},{self.m_col}'] = self.m_object
