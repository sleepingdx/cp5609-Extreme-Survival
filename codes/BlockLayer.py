from codes import MyDefine
from codes.Singelton import Singleton


class BlockLayer(Singleton):
    def __init__(self):
        self.m_blocks = None
        self.m_objects = {}

    def load_blocks(self, json):
        self.m_blocks = json
        self.m_objects = {}
        for row in range(len(self.m_blocks)):
            for col in range(len(self.m_blocks[row])):
                self.m_objects[f'{row},{col}'] = []

    def append(self, row, col, obj, enum):
        if 0 <= row < len(self.m_blocks) and 0 <= col < len(self.m_blocks):
            if self.m_blocks[row][col] != MyDefine.BLOCK_PLACEHOLDERS[1]:
                self.m_blocks[row][col] = enum
            self.m_objects[f'{row},{col}'].append(obj)

    def remove(self, row, col, obj, enum):
        if 0 <= row < len(self.m_blocks) and 0 <= col < len(self.m_blocks):
            if self.m_blocks[row][col] == MyDefine.BLOCK_PLACEHOLDERS[1]:
                self.m_blocks[row][col] = enum
            self.m_objects[f'{row},{col}'].remove(obj)
