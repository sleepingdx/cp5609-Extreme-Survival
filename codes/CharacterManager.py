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
            for key in self.m_characters:
                self.m_characters[key].update()

    def trigger_event(self, event):
        if self.m_characters:
            for key in self.m_characters:
                if hasattr(self.m_characters[key], "trigger_event"):
                    self.m_characters[key].trigger_event(event)

    def append_character(self, character_id, character):
        """
        Append character to dictionary
        :param character_id: Character id
        :param character: Character object
        :return: T/F
        """
        if character_id not in self.m_characters:
            self.m_characters[character_id] = character
            return True
        else:
            return False

    def find_character(self, character_id):
        """
        Find character object by character name
        :param character_id: Character id
        :return: The character object
        """
        return self.m_characters[character_id]

    def delete_character(self, character_id):
        """
        Delete from dictionary
        :param character_id: Character id
        :return: None
        """
        self.m_characters[character_id] = None
