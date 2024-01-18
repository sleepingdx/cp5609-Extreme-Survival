import random

import pygame
from codes import MyDefine
from codes.SpriteManager import SpriteManager
from codes.Vector import Vector
from codes.FSM.FiniteStateMachine import FiniteStateMachine
from codes.BlockLayer import BlockLayer
from codes.PathFinding import PathFinding

MAX_CHARACTER_DIRECTION_COUNT = 4  # Direction of a character
CHARACTER_ACTIONS = ('Stand', 'Move', 'Attack', 'Injured', 'Die')  # Actions
TARGET_TYPES = ("Player", "Npc", "Pet", "Monster")  # Type of attack target


class Character:
    """Basic class of all characters"""
    # Events
    CHARACTER_EVENTS = (
        "EVENT_CHANGE_STATE",
        "EVENT_ON_INJURED"
    )

    def __init__(self, fsm_name):
        # Position
        self.m_position = Vector(0, 0)
        self.m_orientation = Vector(0, 1)
        # Actions
        self.m_spriteMgr = SpriteManager()
        self.m_actions = {}
        self.m_current = 0
        # FSM
        self.m_fsm = FiniteStateMachine(self, fsm_name)
        # Collision
        self.m_collision_rect = MyDefine.BLOCK_COLLIDER_RECT
        # Events
        self.m_events = []
        # Common attributes
        self.m_type = None
        self.m_id = MyDefine.INVALID_ID
        self.m_max_hp = 1
        self.m_hp = self.m_max_hp
        self.m_max_mp = 1
        self.m_mp = self.m_max_mp
        self.m_search_enemy_scope = 0
        self.m_attack_enemy_scope = 0

    def get_current_action(self):
        return self.m_actions[CHARACTER_ACTIONS[self.m_current]]

    def append_action(self, name, action):
        """
        Append action by action name
        :param name: Action name
        :param action: Action object
        :return: None
        """
        self.m_actions[name] = action
        if CHARACTER_ACTIONS[self.m_current] == name:
            self.m_spriteMgr.append_sprite(self.m_actions[CHARACTER_ACTIONS[self.m_current]])

    def change_action(self, index):
        """
        Change the current action
        :param index: index of character's action
        :return: T/F
        """
        if 0 <= index < len(CHARACTER_ACTIONS):
            self.m_spriteMgr.delete_sprite(self.m_actions[CHARACTER_ACTIONS[self.m_current]].m_effect)
            self.m_spriteMgr.delete_sprite(self.m_actions[CHARACTER_ACTIONS[self.m_current]])
            self.m_current = index
            if self.m_actions[CHARACTER_ACTIONS[self.m_current]].m_effect.m_filename != '':
                self.m_spriteMgr.append_sprite(self.m_actions[CHARACTER_ACTIONS[self.m_current]].m_effect)
                self.m_actions[CHARACTER_ACTIONS[self.m_current]].m_effect.set_center_pos(self.m_position.x,
                                                                                          self.m_position.z)
                self.m_actions[CHARACTER_ACTIONS[self.m_current]].m_effect.m_completed = False
                self.m_actions[CHARACTER_ACTIONS[self.m_current]].m_effect.m_frame_index = 0
            self.m_spriteMgr.append_sprite(self.m_actions[CHARACTER_ACTIONS[self.m_current]])
            self.m_actions[CHARACTER_ACTIONS[self.m_current]].m_completed = False
            self.m_actions[CHARACTER_ACTIONS[self.m_current]].m_frame_index = 0
            return True
        else:
            return False

    def update(self):
        self.execute_events()
        self.m_fsm.update()
        self.m_spriteMgr.update()

    def render(self, window):
        self.m_spriteMgr.render(window)

    def draw_health_bar(self, window):
        # 计算血条的宽度
        bar_width = self.get_rect().width
        bar_height = 4

        health_bar_width = int(bar_width * (self.m_hp / self.m_max_hp))
        # 绘制底层血条（红色矩形）
        pygame.draw.rect(window, (192, 192, 192), (self.get_rect().x, self.get_rect().y - 10, bar_width, bar_height),
                         border_radius=2)
        # 绘制实际血量（绿色矩形）
        pygame.draw.rect(window, (0, 255, 0), (self.get_rect().x, self.get_rect().y - 10, health_bar_width, bar_height),
                         border_radius=2)

        magic_bar_width = int(bar_width * (self.m_mp / self.m_max_mp))
        # 绘制底层蓝条（红色矩形）
        pygame.draw.rect(window, (192, 192, 192), (self.get_rect().x, self.get_rect().y - 6, bar_width, bar_height),
                         border_radius=2)
        # 绘制实际蓝量（绿色矩形）
        pygame.draw.rect(window, (0, 0, 255), (self.get_rect().x, self.get_rect().y - 6, magic_bar_width, bar_height),
                         border_radius=2)

    def find_path(self, cls, speed, elapsed_sec):
        if cls.m_path and 0 <= cls.m_current < len(cls.m_path):
            orientation = (cls.m_path[cls.m_current] - self.m_position)
            if orientation.calculate_magnitude2() <= MyDefine.ARRIVE_TARGET_POS_SCOPE ** 2:
                # Find the path
                if len(cls.m_path) > 0 and 0 <= cls.m_current < len(cls.m_path) - 1:
                    if ((self.m_position - cls.m_path[cls.m_current]).calculate_magnitude2() <=
                            MyDefine.ARRIVE_TARGET_POS_SCOPE ** 2):
                        cls.m_current += 1
                        return False
                # Arrived
                return True
            else:
                if len(cls.m_path) > 0 and 0 <= cls.m_current < len(cls.m_path) - 1:
                    blocks = BlockLayer.get_instance().m_blocks
                    objects = BlockLayer.get_instance().m_objects
                    # The current grid is blocked. Need to recalculate a new route
                    cur_row = int(cls.m_path[cls.m_current].z // MyDefine.BLOCK_RESOLUTION[0])
                    cur_col = int(cls.m_path[cls.m_current].x // MyDefine.BLOCK_RESOLUTION[1])
                    if blocks[cur_row][cur_col] != MyDefine.BLOCK_PLACEHOLDERS[0] and len(
                            objects[f'{cur_row},{cur_col}']) > 1:
                        cls.m_current -= 1
                        self.m_fsm.change_state(self.m_fsm.m_last_state)
                        print("Current point is blocked, recalculate a new route.")
                        return True
                    # The next grid is blocked. Need to recalculate a new route.
                    next_row = int(cls.m_path[cls.m_current + 1].z // MyDefine.BLOCK_RESOLUTION[0])
                    next_col = int(cls.m_path[cls.m_current + 1].x // MyDefine.BLOCK_RESOLUTION[1])
                    if blocks[next_row][next_col] != MyDefine.BLOCK_PLACEHOLDERS[0]:
                        cls.m_current -= random.randint(0, 1)
                        self.m_fsm.change_state(self.m_fsm.m_last_state)
                        print("Next point is blocked, recalculate a new route.")
                        return True
                # Velocity
                orientation.normalize()
                self.m_orientation = orientation
                new_pos = (self.m_position + orientation * MyDefine.PIXELS_PER_METER * speed * (elapsed_sec / 1000))
                self.set_center_pos(new_pos.x, new_pos.z)
            return False

    def is_pos_arrived(self, pos):
        blocks = BlockLayer.get_instance().m_blocks
        row_start = min(max(0, int(self.m_position.z // MyDefine.BLOCK_RESOLUTION[0])), len(blocks) - 1)
        col_start = min(max(0, int(self.m_position.x // MyDefine.BLOCK_RESOLUTION[1])), len(blocks[row_start]) - 1)
        row_end = min(max(0, int(pos.z // MyDefine.BLOCK_RESOLUTION[0])), len(blocks) - 1)
        col_end = min(max(0, int(pos.x // MyDefine.BLOCK_RESOLUTION[1])), len(blocks[row_end]) - 1)
        if blocks[row_end][col_end] != MyDefine.BLOCK_PLACEHOLDERS[0]:
            directions = (
                (row_end - 1, col_end),
                (row_end, col_end - 1),
                (row_end + 1, col_end),
                (row_end, col_end + 1)
            )
            for i in range(len(directions)):
                if 0 <= directions[i][0] < len(blocks) and 0 <= directions[i][1] < len(blocks[directions[i][0]]):
                    if blocks[directions[i][0]][directions[i][1]] == MyDefine.BLOCK_PLACEHOLDERS[0]:
                        row_end = directions[i][0]
                        col_end = directions[i][1]
                        break
        return PathFinding.astar_pos(blocks, (row_start, col_start), (row_end, col_end))

    def find_nearest_enemy(self):
        # Find the nearest enemy
        blocks = BlockLayer.get_instance().m_blocks
        row_left = max(0, int((self.m_position.z - self.m_search_enemy_scope * MyDefine.MAP_GRID) //
                              MyDefine.BLOCK_RESOLUTION[0]))
        row_right = min(len(blocks) - 1, int((self.m_position.z + self.m_search_enemy_scope * MyDefine.MAP_GRID) //
                                             MyDefine.BLOCK_RESOLUTION[0]))
        col_top = max(0, int((self.m_position.x - self.m_search_enemy_scope * MyDefine.MAP_GRID) //
                             MyDefine.BLOCK_RESOLUTION[1]))
        col_bottom = min(len(blocks[row_left]) - 1,
                         int((self.m_position.x + self.m_search_enemy_scope * MyDefine.MAP_GRID) //
                             MyDefine.BLOCK_RESOLUTION[1]))
        final_distance2 = None
        target = None
        for row in range(row_left, row_right + 1):
            for col in range(col_top, col_bottom + 1):
                objects = BlockLayer.get_instance().m_objects[f'{row},{col}']
                for i in range(len(objects)):
                    if self != objects[i] and objects[i].m_hp > 0 and objects[i].m_type in TARGET_TYPES:
                        distance = (objects[i].m_position - self.m_position).calculate_magnitude2()
                        if not final_distance2:
                            final_distance2 = distance
                        elif distance <= final_distance2:
                            final_distance2 = distance
                        if distance <= (objects[i].m_search_enemy_scope * MyDefine.MAP_GRID) ** 2:
                            target = objects[i]
        return target, final_distance2

    def set_center_pos(self, x, z):
        self.m_position = Vector(x, z)

    def get_current_speed(self):
        return self.m_fsm.get_current_state().m_speed

    def get_rect(self):
        return self.m_actions[CHARACTER_ACTIONS[self.m_current]].rect

    def attack(self, target):
        if target:
            self.m_fsm.change_state(5, target)
            target.onDamaged(target.m_max_hp * 2 / 100)

    def onDamaged(self, value):
        self.m_hp = max(0, self.m_hp - value)
        self.m_fsm.change_state(6)

    def onDied(self):
        self.m_fsm.change_state(7)

    def is_action_completed(self, index):
        if self.m_actions[CHARACTER_ACTIONS[index]].m_completed:
            return True
        return False

    def push_event(self, event):
        if event:
            self.m_events.append(event)

    def execute_events(self):
        events_to_remove = []
        for event in self.m_events:
            if event[0] == Character.CHARACTER_EVENTS[0]:
                self.m_fsm.change_state(event[1], event[2])
            elif event[0] == Character.CHARACTER_EVENTS[1]:
                self.onDamaged(event[1])
            else:
                pass
            events_to_remove.append(event)
        for event in events_to_remove:
            self.m_events.remove(event)
