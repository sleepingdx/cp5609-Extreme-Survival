import time
from codes import MyDefine
from codes.SpriteManager import SpriteManager
from codes.Vector import Vector
from codes.FSM.FiniteStateMachine import FiniteStateMachine

# Direction of a character
MAX_CHARACTER_DIRECTION_COUNT = 4
# Actions
CHARACTER_ACTIONS = ('Stand', 'Move', 'Attack', 'Damage', 'Die')


class Character:
    """Basic class of all characters"""

    def __init__(self):
        # Position
        self.m_position = Vector(0, 0)
        self.m_orientation = Vector(0, 0)
        # Actions
        self.m_spriteMgr = SpriteManager()
        self.m_actions = {}
        self.m_current = 0
        # FSM
        self.m_fsm = FiniteStateMachine(self, "Character")
        self.m_target_pos = Vector(0, 0)
        self.m_sec = MyDefine.convert_nsec_to_msec(time.time_ns())
        # Collision
        self.m_collision_rect = MyDefine.BLOCK_COLLIDER_RECT
        #
        self.m_id = MyDefine.INVALID_ID
        self.m_row = MyDefine.INVALID_ID
        self.m_col = MyDefine.INVALID_ID
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

    def set_center_pos(self, x, z):
        self.m_position = Vector(x, z)

    def get_rect(self):
        return self.m_actions[CHARACTER_ACTIONS[self.m_current]].rect

    def attack(self, obj):
        self.m_fsm.change_status(2)
        if obj:
            obj.onDamaged(-10)

    def onDamaged(self, hp):
        self.m_hp += hp
        self.m_fsm.change_status(3)

    def onDied(self):
        self.m_fsm.change_status(4)

    def is_action_completed(self, index):
        if self.m_actions[CHARACTER_ACTIONS[index]].m_completed:
            return True
        return False
