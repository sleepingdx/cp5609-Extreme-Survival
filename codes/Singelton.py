class Singleton:
    """Singleton module"""
    m_instances = {}

    @classmethod
    def getInstance(cls):
        if cls not in cls.m_instances:
            cls.m_instances[cls] = cls()
        return cls.m_instances[cls]
