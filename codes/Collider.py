from codes import MyDefine


class Collider:
    def __init__(self, pos, radius, obj, blocks):
        self.m_position = pos
        self.m_radius = radius
        self.m_object = obj
        self.m_blocks = blocks
        self.m_row = MyDefine.INVALID_ID
        self.m_col = MyDefine.INVALID_ID

    def update(self):
        pos = self.m_object.m_position
        row = pos % MyDefine.BL

