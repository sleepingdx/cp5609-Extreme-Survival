import pygame
import time
from codes import MyDefine
from codes.FSM.State import State
from codes.BlockLayer import BlockLayer
from codes.PathFinding import PathFinding
from codes.JsonManager import JsonManager
from codes.CollideDection import CollideDetection

CONST_DEVIATION = 5  # the deviation of collide detection


class Move(State):
    def __init__(self, obj):
        super().__init__(obj)
        self.m_target_pos = self.m_object.m_position
        self.m_orientation = self.m_object.m_orientation
        self.m_path = []
        self.m_current = 0
        self.m_pathfinding = False
        self.m_sec = 0

    def begin(self, pos):
        super().begin(pos)
        self.m_path.clear()
        self.m_current = 0
        # Position
        if pos:
            if (pos - self.m_object.m_position).calculate_magnitude2() <= (MyDefine.MAP_GRID * 3) ** 2:
                self.m_pathfinding = False
                self.m_target_pos = pos
            else:
                self.m_pathfinding = True
                blocks = BlockLayer.get_instance().m_blocks
                row = int(pos.z // MyDefine.BLOCK_RESOLUTION[0])
                col = int(pos.x // MyDefine.BLOCK_RESOLUTION[1])
                if blocks[row][col] != MyDefine.BLOCK_PLACEHOLDERS[0]:
                    directions = (
                        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1),
                        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1))
                    for i in range(len(directions)):
                        if 0 <= directions[i][0] < len(blocks) and 0 <= directions[i][1] < len(
                                blocks[directions[i][0]]):
                            if blocks[directions[i][0]][directions[i][1]] == MyDefine.BLOCK_PLACEHOLDERS[0]:
                                row = directions[i][0]
                                col = directions[i][1]
                                break
                self.m_path = PathFinding.astar_pos(blocks, (self.m_row, self.m_col), (row, col))
                if len(self.m_path) > 0:
                    del self.m_path[0]
            # Action
            self.m_object.change_action(1)
            self.m_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
        else:
            self.m_object.m_fsm.change_state(0)

    def update(self):
        super().update()

        if not self.m_pathfinding:
            self.m_orientation = (self.m_target_pos - self.m_object.m_position)
            # Arrived
            if self.m_orientation.calculate_magnitude2() <= MyDefine.ARRIVE_TARGET_POS_SCOPE ** 2:
                # Already arrived the destination
                self.m_object.m_fsm.change_state(0)
                return
        else:
            if len(self.m_path) > 0:
                self.m_orientation = (self.m_path[self.m_current] - self.m_object.m_position)

        # Velocity
        current_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
        elapsed_sec = current_sec - self.m_sec
        self.m_sec = current_sec

        self.m_orientation.normalize()
        self.m_object.m_orientation = self.m_orientation
        new_pos = (self.m_object.m_position + self.m_orientation * MyDefine.PIXELS_PER_METER
                   * MyDefine.BASIC_CHARACTER_MOVE_SPEED * (elapsed_sec / 1000))

        if not self.m_pathfinding:
            # Perform collision detection only during free movement
            from codes.GameLevelManager import GameLevelManager
            from codes.GameLevel import GameLevel
            from codes.TerrainManager import TerrainManager
            # Collision Detection
            blocks = BlockLayer.get_instance().m_blocks
            for r in range(max(0, self.m_row - 1), min(self.m_row + 1 + 1, len(blocks))):
                for c in range(max(0, self.m_col - 1), min(self.m_col + 1 + 1, len(blocks[r]))):
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
                                                                    self.m_orientation * CONST_DEVIATION,
                                                                    terrain.mask_layer_2[r][c], rect):
                                self.m_object.m_fsm.change_state(0)
                                return
                    elif blocks[r][c] == MyDefine.BLOCK_PLACEHOLDERS[2]:
                        objects = BlockLayer.get_instance().m_objects[f'{r},{c}']
                        if objects:
                            for i in range(len(objects)):
                                if objects[i] and objects[i] != self.m_object:
                                    # Pixel collide detection
                                    if CollideDetection.detect_mask_collide(self.m_object.get_current_action(),
                                                                            self.m_orientation * CONST_DEVIATION,
                                                                            objects[i].get_current_action().mask,
                                                                            objects[i].get_current_action().rect):
                                        self.m_object.m_fsm.change_state(0)
                                        return
            self.m_object.set_center_pos(new_pos.x, new_pos.z)
        else:
            # Do not perform collision detection only during free movement
            if self.m_object.path_finding(self, new_pos):
                self.m_object.m_fsm.change_state(0)

    def end(self):
        self.m_target_pos = self.m_object.m_position
        self.m_path.clear()
        self.m_current = 0
        self.m_pathfinding = False
        return super().end()
