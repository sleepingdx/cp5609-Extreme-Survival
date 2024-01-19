import os
from codes import MyDefine
from codes.Singelton import Singleton
from codes.Json import Json

JSON_GAME_LEVEL_FILE = os.path.join(MyDefine.get_current_path(), "res/json/gameLevels.json")
JSON_CHARACTERS_FILE = os.path.join(MyDefine.get_current_path(), "res/json/characters.json")
JSON_FSM_FILE = os.path.join(MyDefine.get_current_path(), "res/json/fsm.json")
JSON_TERRAIN_FILE = os.path.join(MyDefine.get_current_path(), "res/json/terrain.json")


class JsonManager(Singleton):
    def __init__(self):
        self.m_json_gameLevels = Json().load_json(JSON_GAME_LEVEL_FILE, "r")
        self.m_json_characters = Json().load_json(JSON_CHARACTERS_FILE, "r")
        self.m_json_fsm = Json().load_json(JSON_FSM_FILE, "r")
        self.m_json_terrain = Json().load_json(JSON_TERRAIN_FILE, "r")
