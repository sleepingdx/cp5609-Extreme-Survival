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
        self.m_curAction = 0

    def appendAction(self, name, action):
        """
        Append action by action name
        :param name: Action name
        :param action: Action object
        :return: None
        """
        self.m_actions[name] = action

    def changeAction(self, index):
        """
        Change the current action
        :param index: index of character's action
        :return: T/F
        """
        if 0 <= index < len(CHARACTER_ACTIONS):
            self.m_curAction = index
            return True
        else:
            return False

    def update(self):
        pass

    def setCenterPos(self, x, z):
        self.m_actions[self.m_curAction].setCenterPos(x, z)
