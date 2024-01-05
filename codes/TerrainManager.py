from codes.Singelton import Singleton
from codes.JsonManager import JsonManager
from codes.Terrain import Terrain


class TerrainManager(Singleton):
    def __init__(self):
        self.m_terrains = []
        self.m_current = 0

    def load_terrain(self, index):
        json_terrains = JsonManager.get_instance().m_json_terrain
        if 0 <= index < len(json_terrains):
            self.m_terrains.append(Terrain(json_terrains[index]))

    def remove_terrain(self, index):
        if 0 <= index < len(self.m_terrains):
            del self.m_terrains[index]

    def change_terrain(self, index):
        if 0 <= index < len(self.m_terrains):
            self.m_current = index

    def get_terrain(self, index):
        if 0 <= index < len(self.m_terrains):
            return self.m_terrains[index]

    def update(self):
        if 0 <= self.m_current < len(self.m_terrains):
            self.m_terrains[self.m_current].update()

    def render(self, window):
        if 0 <= self.m_current < len(self.m_terrains):
            self.m_terrains[self.m_current].render(window)
