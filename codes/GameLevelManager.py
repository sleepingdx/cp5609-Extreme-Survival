from codes.Singelton import Singleton


class GameLevelManager(Singleton):
    """Centralized management of all game levels"""

    def __init__(self):
        self.m_gameLevels = []

    def appendGameLevel(self, obj):
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

    def deleteGameLevel(self, obj):
        """
        Remove object from list
        :param obj: Object of game level
        :return: T/F
        """
        return self.m_gameLevels.remove(obj)
