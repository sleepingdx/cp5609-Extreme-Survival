from codes.SpriteManager import SpriteManager
from codes.Vector import Vector

# Direction of a character
MAX_CHARACTER_DIRECTION_COUNT = 4
# Basic move speed (m/s)
BASIC_CHARACTER_MOVE_SPEED = 0.5
# Actions
CHARACTER_ACTIONS = ('stand', 'move', 'attack', 'die')


class Character:
    """Basic class of all characters"""

    def __init__(self):
        super().__init__()
        # Position
        self.m_position = Vector(0, 0)
        self.m_x = 0
        self.m_z = 0
        # Actions
        self.m_actions = {}
        self.m_current = 0

    def append_action(self, name, action):
        """
        Append action by action name
        :param name: Action name
        :param action: Action object
        :return: None
        """
        self.m_actions[name] = action
        if CHARACTER_ACTIONS[self.m_current] == name:
            SpriteManager.get_instance().append_sprite(self.m_actions[CHARACTER_ACTIONS[self.m_current]])

    def change_action(self, index):
        """
        Change the current action
        :param index: index of character's action
        :return: T/F
        """
        if 0 <= index < len(CHARACTER_ACTIONS):
            SpriteManager.get_instance().delete_sprite(self.m_actions[CHARACTER_ACTIONS[self.m_current]])
            self.m_current = index
            SpriteManager.get_instance().append_sprite(self.m_actions[CHARACTER_ACTIONS[self.m_current]])
            return True
        else:
            return False

    def update(self):
        pass

    def set_center_pos(self, x, z):
        self.m_position = Vector(x, z)
