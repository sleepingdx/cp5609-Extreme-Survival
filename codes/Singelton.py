class Singleton:
    """Singleton module"""
    m_instances = {}

    @classmethod
    def get_instance(cls):
        if cls not in cls.m_instances:
            cls.m_instances[cls] = cls()
        return cls.m_instances[cls]
