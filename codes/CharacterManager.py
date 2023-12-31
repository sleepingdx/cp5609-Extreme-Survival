from codes.Singelton import Singleton


class CharacterManager(Singleton):
    """Centralized management of all character objects"""

    def __init__(self):
        self.m_characters = {}

    def update(self):
        """
        Update all registered characters by using the update method of each character
        :return: None
        """
        if self.m_characters:
            for i in range(len(self.m_characters)):
                self.m_characters[i].update()

    def append_character(self, name, character):
        """
        Append character to dictionary
        :param name: Character name
        :param character: Character object
        :return: T/F
        """
        if ~self.m_characters[name]:
            self.m_characters[name] = character
            return True
        else:
            return False

    def find_character(self, name):
        """
        Find character object by character name
        :param name: Character name
        :return: The character object
        """
        return self.m_characters[name]

    def delete_character(self, name):
        """
        Delete from dictionary
        :param name: Character name
        :return: None
        """
        self.m_characters[name] = None
