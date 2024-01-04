from codes.Singelton import Singleton
from codes import MyDefine
from codes.Json import Json


class JsonManager(Singleton):
    def __init__(self):
        self.m_json_gameLevels = Json().load_json(MyDefine.JSON_GAME_LEVEL_FILE, "r")
        self.m_json_characters = Json().load_json(MyDefine.JSON_CHARACTERS_FILE, "r")
        self.m_json_fsm = Json().load_json(MyDefine.JSON_FSM_FILE, "r")
        self.m_json_terrain = Json().load_json(MyDefine.JSON_TERRAIN_FILE, "r")
