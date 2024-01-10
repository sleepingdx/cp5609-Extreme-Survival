from codes import MyDefine
from codes.GlobalVariables import GlobalVariables
from codes.JsonManager import JsonManager
from codes.Action import Action
from codes.CharacterManager import CharacterManager
from codes.TerrainManager import TerrainManager
from codes.BlockLayer import BlockLayer
from codes.Character import Character
from codes.Player import Player
from codes.Npc import Npc
from codes.Item import Item
from codes.Equipment import Equipment

CHARACTERS_KEY = "characters"
TERRAIN_KEY = "terrain"


class GameLevel:
    def __init__(self, index):
        self.m_index = index

    def start(self):
        # Terrain
        terrain_index = JsonManager.get_instance().m_json_gameLevels[self.m_index][TERRAIN_KEY]
        TerrainManager.get_instance().load_terrain(terrain_index)
        TerrainManager.get_instance().change_terrain(terrain_index)
        # block layer
        json_blocks = JsonManager.get_instance().m_json_terrain[terrain_index]['block_layer']
        BlockLayer.get_instance().load_blocks(json_blocks)
        # Characters
        characters = JsonManager.get_instance().m_json_characters
        objects = JsonManager.get_instance().m_json_gameLevels[self.m_index][CHARACTERS_KEY]
        for i in range(len(objects) - 1, -1, -1):
            if objects[i]["id"] == MyDefine.INVALID_ID:
                objects[i]["id"] = GlobalVariables.get_instance().m_role_id
            for j in range(len(characters)):
                if characters[j]["id"] == objects[i]["id"]:
                    character = globals()[characters[j]["type"]]()
                    CharacterManager.get_instance().append_character(objects[i]["id"], character)
                    for k in range(len(characters[j]["actions"])):
                        action = Action(character, characters[j]["actions"][k]["filename"])
                        action.m_orientation = objects[i]["orientation"]
                        character.append_action(characters[j]["actions"][k]["name"], action)
                        for l in range(len(characters[j]["actions"][k]["frames"])):
                            action.load_action_from_list(characters[j]["actions"][k]["frames"][l]["name"],
                                                         characters[j]["actions"][k]["frames"][l]["list"],
                                                         characters[j]["resolution"])
                    character.set_center_pos(objects[i]["position"][0], objects[i]["position"][1])

    def update(self):
        pass

    def end(self):
        pass
