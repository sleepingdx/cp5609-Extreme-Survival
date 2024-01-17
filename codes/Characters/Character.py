import pygame
from codes import MyDefine
from codes.SpriteManager import SpriteManager
from codes.Vector import Vector
from codes.FSM.FiniteStateMachine import FiniteStateMachine

MAX_CHARACTER_DIRECTION_COUNT = 4  # Direction of a character
CHARACTER_ACTIONS = ('Stand', 'Move', 'Attack', 'Injured', 'Die')  # Actions


class Character:
    """Basic class of all characters"""

    def __init__(self, fsm_name):
        # Position
        self.m_position = Vector(0, 0)
        self.m_orientation = Vector(0, 0)
        # Actions
        self.m_spriteMgr = SpriteManager()
        self.m_actions = {}
        self.m_current = 0
        # FSM
        self.m_fsm = FiniteStateMachine(self, fsm_name)
        # Collision
        self.m_collision_rect = MyDefine.BLOCK_COLLIDER_RECT
        #
        self.m_id = MyDefine.INVALID_ID
        self.m_max_hp = 1
        self.m_hp = self.m_max_hp
        self.m_max_mp = 1
        self.m_mp = self.m_max_mp

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

    def find_path(self, cls, new_pos):
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
                # Velocity
                orientation.normalize()
                self.m_orientation = orientation
            self.set_center_pos(new_pos.x, new_pos.z)
            return False

    def set_center_pos(self, x, z):
        self.m_position = Vector(x, z)

    def get_rect(self):
        return self.m_actions[CHARACTER_ACTIONS[self.m_current]].rect

    def attack(self, obj):
        self.m_fsm.change_state(5)
        if obj:
            obj.onDamaged(-10)

    def onDamaged(self, hp):
        self.m_hp += hp
        self.m_fsm.change_state(6)

    def onDied(self):
        self.m_fsm.change_state(7)

    def is_action_completed(self, index):
        if self.m_actions[CHARACTER_ACTIONS[index]].m_completed:
            return True
        return False
