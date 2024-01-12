import pygame
import time
from codes import MyDefine
from codes.FSM.State import State
from codes.BlockLayer import BlockLayer
from codes.JsonManager import JsonManager
from codes.CollideDection import CollideDetection

CONST_DEVIATION = 5


class Move(State):
    def __init__(self, obj):
        super().__init__(obj)

    def begin(self):
        super().begin()
        self.m_object.change_action(1)
        self.m_object.m_sec = MyDefine.convert_nsec_to_msec(time.time_ns())

    def update(self):
        super().update()
        current_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
        elapsed_sec = current_sec - self.m_object.m_sec
        self.m_object.m_sec = current_sec

        orientation = (self.m_object.m_target_pos - self.m_object.m_position)
        if orientation.calculate_magnitude2() <= MyDefine.ARRIVE_TARGET_POS_RANGE ** 2:
            self.m_object.m_fsm.change_status(0)
            return
        else:
            from codes.GameLevelManager import GameLevelManager
            from codes.GameLevel import GameLevel
            from codes.TerrainManager import TerrainManager
            orientation.normalize()
            self.m_object.m_orientation = orientation
            new_pos = (self.m_object.m_position + orientation * MyDefine.PIXELS_PER_METER *
                       MyDefine.BASIC_CHARACTER_MOVE_SPEED * (elapsed_sec / 1000))
            # Collision Detection
            blocks = BlockLayer.get_instance().m_blocks
            for r in range(max(0, self.m_object.m_row - 1), min(self.m_object.m_row + 1 + 1, len(blocks))):
                for c in range(max(0, self.m_object.m_col - 1), min(self.m_object.m_col + 1 + 1, len(blocks[r]))):
                    if blocks[r][c] == MyDefine.BLOCK_PLACEHOLDERS[1]:
                        terrain_index = \
                            JsonManager.get_instance().m_json_gameLevels[GameLevelManager.get_instance().m_current][
                                GameLevel.TERRAIN_KEY]
                        terrain = TerrainManager.get_instance().get_terrain(terrain_index)
                        rect = pygame.Rect(c * MyDefine.TILE_RESOLUTION[0], r * MyDefine.TILE_RESOLUTION[1],
                                           MyDefine.TILE_RESOLUTION[0], MyDefine.TILE_RESOLUTION[1])
                        # Pixel collide detection
                        if terrain.mask_layer_2[r][c]:
                            if CollideDetection.detect_mask_collide(self.m_object.get_current_action(),
                                                                    orientation * CONST_DEVIATION,
                                                                    terrain.mask_layer_2[r][c], rect):
                                self.m_object.m_fsm.change_status(0)
                                return
                    elif blocks[r][c] == MyDefine.BLOCK_PLACEHOLDERS[2]:
                        objects = BlockLayer.get_instance().m_objects[f'{r},{c}']
                        if objects:
                            for i in range(len(objects)):
                                if objects[i] and objects[i] != self.m_object:
                                    # Pixel collide detection
                                    if CollideDetection.detect_sprite_collide(self.m_object.get_current_action(),
                                                                              orientation * CONST_DEVIATION,
                                                                              [objects[i].m_spriteMgr.m_sprites]):
                                        self.m_object.m_fsm.change_status(0)
                                        # self.m_object.set_center_pos(500, 500)
                                        return
        self.m_object.set_center_pos(new_pos.x, new_pos.z)

    def end(self):
        super().end()
