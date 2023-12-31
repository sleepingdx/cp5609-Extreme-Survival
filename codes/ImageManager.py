import pygame.image
from codes.Singelton import Singleton


class ImageManager(Singleton):
    """Centralized management of all imaging resources"""

    def __init__(self):
        self.m_resDirectory = {}  # Resource Directory

    def load_resource(self, name, file):
        """
        Load resource and add to resource directory
        :param name: Resource name
        :param file: Resource File directory
        :return: None
        """
        if ~self.m_resDirectory[name]:
            image = pygame.image.load(file).convert()
            # file: the image file name
            # image: the image resource
            self.m_resDirectory[name]: {'file': file, 'image': image}

    def find_resource_by_name(self, name):
        """
        Find the image by using resource name
        :param name: Resource name
        :return: Tuple contained resource path and loaded image
        """
        return self.m_resDirectory[name]
