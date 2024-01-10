import math
import random
from codes import MyDefine
from codes.ImageManager import ImageManager


class Terrain:
    def __init__(self, json):
        self.terrain = []
        self.m_id = json['id']
        self.m_name = json['name']
        self.m_files = []
        for i in range(len(json['filenames'])):
            self.m_files.append(json['filenames'][i])
            ImageManager.get_instance().load_resource(json['filenames'][i], json['filenames'][i])
        # Base layer 1
        self.base_layer_1 = []
        for r in range(len(json['base_layer_1'])):
            row = []
            for c in range(len(json['base_layer_1'][r])):
                col = json['base_layer_1'][r][c]
                row.append(col)
            self.base_layer_1.append(row)
        # Base layer 2
        self.base_layer_2 = []
        for r in range(len(json['base_layer_2'])):
            row = []
            for c in range(len(json['base_layer_2'][r])):
                col = json['base_layer_2'][r][c]
                row.append(col)
            self.base_layer_2.append(row)
        # Masking layer
        self.m_masking_layer = []
        for r in range(len(json['masking_layer'])):
            row = []
            for c in range(len(json['masking_layer'][r])):
                col = json['masking_layer'][r][c]
                row.append(col)
            self.m_masking_layer.append(row)

    def update(self):
        pass

    def render_base_layer_1(self, window):
        for row in range(len(self.base_layer_1)):
            for col in range(len(self.base_layer_1[row])):
                res = ImageManager.get_instance().find_resource_by_name(self.m_files[self.base_layer_1[row][col][0]])
                window.blit(res["image"],
                            (col * MyDefine.TILE_RESOLUTION[0] - 6, row * MyDefine.TILE_RESOLUTION[1] - 6),
                            (self.base_layer_1[row][col][1][1] * MyDefine.TILE_RESOLUTION[0],
                             self.base_layer_1[row][col][1][0] * MyDefine.TILE_RESOLUTION[1],
                             MyDefine.TILE_RESOLUTION[0],
                             MyDefine.TILE_RESOLUTION[1]))

    def render_base_layer_2(self, window):
        for row in range(len(self.base_layer_2)):
            for col in range(len(self.base_layer_2[row])):
                if self.base_layer_2[row][col][0] != MyDefine.INVALID_ID:
                    res = ImageManager.get_instance().find_resource_by_name(
                        self.m_files[self.base_layer_2[row][col][0]])
                    window.blit(res["image"],
                                (col * MyDefine.TILE_RESOLUTION[0] - 6, row * MyDefine.TILE_RESOLUTION[1] - 6),
                                (self.base_layer_2[row][col][1][1] * MyDefine.TILE_RESOLUTION[0],
                                 self.base_layer_2[row][col][1][0] * MyDefine.TILE_RESOLUTION[1],
                                 MyDefine.TILE_RESOLUTION[0],
                                 MyDefine.TILE_RESOLUTION[1]))

    def render_masking_layer(self, window):
        for row in range(len(self.m_masking_layer)):
            for col in range(len(self.m_masking_layer[row])):
                if self.m_masking_layer[row][col][0] != MyDefine.INVALID_ID:
                    res = ImageManager.get_instance().find_resource_by_name(
                        self.m_files[self.m_masking_layer[row][col][0]])
                    window.blit(res["image"],
                                (col * MyDefine.TILE_RESOLUTION[0] - 6, row * MyDefine.TILE_RESOLUTION[1] - 6),
                                (self.m_masking_layer[row][col][1][1] * MyDefine.TILE_RESOLUTION[0],
                                 self.m_masking_layer[row][col][1][0] * MyDefine.TILE_RESOLUTION[1],
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
