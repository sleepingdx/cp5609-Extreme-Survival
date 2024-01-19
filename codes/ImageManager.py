import pygame.image
import sys
import os
from codes.Singelton import Singleton
from codes import MyDefine


class ImageManager(Singleton):
    """Centralized management of all imaging resources"""

    def __init__(self):
        self.m_resDirectory = {}  # Resource Directory

    def load_resource(self, name, filename):
        """
        Load resource and add to resource directory
        :param name: Resource name
        :param filename: Resource File directory
        :return: None
        """
        if name not in self.m_resDirectory:
            path = MyDefine.get_current_dir(filename)
            image = pygame.image.load(path)
            # file: the image file name image: the image resource
            self.m_resDirectory[name] = {'filename': filename, 'image': image}

    def find_resource_by_name(self, name):
        """
        Find the image by using resource name
        :param name: Resource name
        :return: Tuple contained resource path and loaded image
        """
        return self.m_resDirectory[name]
