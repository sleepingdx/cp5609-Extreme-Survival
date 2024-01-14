from codes import MyDefine
from codes.GlobalVariables import GlobalVariables
from codes.JsonManager import JsonManager
from codes.Action import Action
from codes.TerrainManager import TerrainManager
from codes.BlockLayer import BlockLayer
from codes.Effect import Effect
from codes.characters.CharacterManager import CharacterManager
from codes.characters.Character import Character
from codes.characters.Player import Player
from codes.characters.Npc import Npc
from codes.characters.Merchant import Merchant
from codes.characters.Monster import Monster
from codes.characters.Pet import Pet
from codes.characters.Equipment import Equipment
from codes.characters.Item import Item


class GameLevel:
    CHARACTERS_KEY = "characters"
    TERRAIN_KEY = "terrain"

    def __init__(self, index):
        self.m_index = index

    def start(self):
        # Terrain
        terrain_index = JsonManager.get_instance().m_json_gameLevels[self.m_index][GameLevel.TERRAIN_KEY]
        TerrainManager.get_instance().load_terrain(terrain_index)
        TerrainManager.get_instance().change_terrain(terrain_index)
        # block layer
        json_blocks = JsonManager.get_instance().m_json_terrain[terrain_index]['block_layer']
        BlockLayer.get_instance().load_blocks(json_blocks)
        # Characters
        characters = JsonManager.get_instance().m_json_characters
        objects = JsonManager.get_instance().m_json_gameLevels[self.m_index][GameLevel.CHARACTERS_KEY]
        for i in range(len(objects) - 1, -1, -1):
            if objects[i]["id"] == MyDefine.INVALID_ID:
                objects[i]["id"] = GlobalVariables.get_instance().m_role_id
            for j in range(len(characters)):
                if characters[j]["id"] == objects[i]["id"]:
                    character = globals()[characters[j]["type"]]()
                    character.m_collision_rect = characters[j]["collision_rect"]
                    character.m_id = characters[j]["id"]
                    character.m_max_hp = characters[j]['hp']
                    character.m_hp = character.m_max_hp
                    character.m_max_mp = characters[j]['mp']
                    character.m_mp = character.m_max_mp
                    CharacterManager.get_instance().append_character(objects[i]["id"], character)
                    for k in range(len(characters[j]["actions"])):
                        action = Action(character, characters[j]["actions"][k]["filename"])
                        action.m_orientation = objects[i]["orientation"]
                        character.append_action(characters[j]["actions"][k]["name"], action)
                        for l in range(len(characters[j]["actions"][k]["frames"])):
                            action.load_action_from_list(characters[j]["actions"][k]["frames"][l]["name"],
                                                         characters[j]["actions"][k]["frames"][l]["list"],
                                                         characters[j]["resolution"])
                            action.m_effect = Effect(characters[j]["actions"][k]["effect"]["filename"])
                            action.m_effect.load_frames(characters[j]["actions"][k]["effect"]["frames"],
                                                        characters[j]["actions"][k]["effect"]["resolution"])
                    character.set_center_pos(objects[i]["position"][0], objects[i]["position"][1])

    def update(self):
        pass

    def end(self):
        pass
