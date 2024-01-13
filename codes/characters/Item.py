from codes.characters.Character import Character


class Item(Character):
    """Items that fall to the ground can be picked up"""

    def __init__(self):
        super().__init__()
