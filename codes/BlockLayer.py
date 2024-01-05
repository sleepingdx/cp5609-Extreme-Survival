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
                self.m_objects[f'{row},{col}'] = None

    def hold_place(self, row, col, obj, enum):
        if self.m_blocks[row][col] and self.m_blocks[row][col] == 0:
            self.m_blocks[row][col] = enum
            if enum == MyDefine.BLOCK_PLACEHOLDERS[2]:
                self.m_objects[f'{row},{col}'] = obj
