import math
import random
from codes import MyDefine


class Terrain:
    def __init__(self):
        """Constructive method"""
        self.terrain = []

    def generate_terrain(self, width, height, obstacles):
        """
        Generate random terrain
        width - the number of horizontal pixels
        height - the number of horizontal pixels
        obstacles - refers to an array contained the type of obstacles
        """
        # Calculate grid number of a row and col
        rowGrids = math.floor(width / MyDefine.MAP_GRID)
        colGrids = math.floor(height / MyDefine.MAP_GRID)
        for row in range(rowGrids):
            for col in range(colGrids):
                self.terrain.append(0)

        # produce random obstacles
        for i in range(obstacles.len()):
            row = random.randint(0, rowGrids - 1)
            col = random.randint(0, colGrids - 1)
            self.terrain[row * colGrids + col] = 1
