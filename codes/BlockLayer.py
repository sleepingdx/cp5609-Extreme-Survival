from codes import MyDefine


class BlockLayer:
    def __init__(self, json):
        self.m_blocks = json['blocks']
        self.m_objects = {}
        for row in range(len(self.m_blocks)):
            for col in range(len(self.m_blocks[row])):
                self.m_objects[f'{row},{col}'] = None

    def hold_place(self, row, col, obj, enum):
        if self.m_blocks[row][col] and self.m_blocks[row][col] == 0:
            self.m_blocks[row][col] = enum
            if enum == MyDefine.BLOCK_PLACEHOLDERS[2]:
                self.m_objects[f'{row},{col}'] = obj
