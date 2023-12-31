from codes.Singelton import Singleton


class GameLevelManager(Singleton):
    """Centralized management of all game levels"""

    def __init__(self):
        self.m_gameLevels = []
        self.m_current = 0

    def append_character(self, obj):
        pass

    def append_terrain(self, obj):
        pass

    def start(self, index):
        """
        Start the current game leve
        :param index: index of current game level
        :return: T/F
        """
        if 0 <= index < len(self.m_gameLevels):
            self.m_current = index
            self.m_gameLevels[self.m_current].start()
            return True
        else:
            return False

    def update(self):
        """
        Update the current game level
        :return:
        """
        self.m_gameLevels[self.m_current].update()

    def end(self):
        """
        End the current game level
        :return:
        """
        self.m_gameLevels[self.m_current].end()

    def append_game_level(self, obj):
        """
        Append new game level
        :param obj: object of game level
        :return: T/F
        """
        if obj not in self.m_gameLevels:
            self.m_gameLevels.append(obj)
            return True
        else:
            return False

    def delete_game_level(self, obj):
        """
        Remove object from list
        :param obj: Object of game level
        :return: T/F
        """
        return self.m_gameLevels.remove(obj)
