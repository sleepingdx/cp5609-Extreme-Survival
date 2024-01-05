import math
import random
from codes import MyDefine
from codes.ImageManager import ImageManager
from codes.BlockLayer import BlockLayer


class Terrain:
    def __init__(self, json):
        self.terrain = []
        self.m_id = json['id']
        self.m_name = json['name']
        self.m_files = []
        for i in range(len(json['filenames'])):
            self.m_files.append(json['filenames'][i])
            ImageManager.get_instance().load_resource(json['filenames'][i], json['filenames'][i])
        self.m_tiles = []
        for r in range(len(json['tiles'])):
            row = []
            for c in range(len(json['tiles'][r])):
                col = json['tiles'][r][c]
                row.append(col)
            self.m_tiles.append(row)
        self.m_block_layer = BlockLayer(json)

    def update(self):
        pass

    def render(self, window):
        for row in range(len(self.m_tiles)):
            for col in range(len(self.m_tiles[row])):
                res = ImageManager.get_instance().find_resource_by_name(self.m_files[self.m_tiles[row][col][0]])
                window.blit(res["image"], (col * MyDefine.TILE_RESOLUTION[0], row * MyDefine.TILE_RESOLUTION[1]),
                            (self.m_tiles[row][col][1][1] * MyDefine.TILE_RESOLUTION[0],
                             self.m_tiles[row][col][1][0] * MyDefine.TILE_RESOLUTION[1],
                             MyDefine.TILE_RESOLUTION[0],
                             MyDefine.TILE_RESOLUTION[1]))

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
