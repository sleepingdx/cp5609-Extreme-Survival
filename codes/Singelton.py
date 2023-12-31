class Singleton:
    """Singleton module"""

    def __init__(self):
        pass

    @staticmethod
    def getInstance():
        return singleton_instance


singleton_instance = Singleton()
