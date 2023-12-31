# Direction of a character
MAX_CHARACTER_DIRECTION_COUNT = 4
# Basic move speed (m/s)
BASIC_CHARACTER_MOVE_SPEED = 0.5
# Actions
CHARACTER_ACTIONS = ('Stand', 'Move', 'Attack', 'Die')


class Character:
    """Basic class of all characters"""

    def __init__(self):
        super().__init__()
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

    def change_action(self, index):
        """
        Change the current action
        :param index: index of character's action
        :return: T/F
        """
        if 0 <= index < len(CHARACTER_ACTIONS):
            self.m_current = index
            return True
        else:
            return False

    def update(self):
        pass

    def set_center_pos(self, x, z):
        self.m_actions[self.m_current].set_center_pos(x, z)
