from codes.JsonManager import JsonManager
from codes.FSM.Idle import Idle
from codes.FSM.Move import Move
from codes.FSM.Patrol import Patrol
from codes.FSM.Chase import Chase
from codes.FSM.Flee import Flee
from codes.FSM.Attack import Attack
from codes.FSM.Injured import Injured
from codes.FSM.Death import Death
from codes.FSM.Interact import Interact

# The order of states is significantly important.
# Please do not move easily, but you could push a new one at the end of list.
ENUM_FSM_STATES = ["Idle", "Move", "Patrol", "Chase", "Flee", "Attack", "Injured", "Death", "Interact"]


class FiniteStateMachine:
    def __init__(self, obj, fsm_type):
        self.m_states = {}
        self.m_current = 0
        self.m_last_state = self.m_current
        # Initialize states
        self.m_fsm = JsonManager.get_instance().m_json_fsm[fsm_type]
        for key in self.m_fsm.keys():
            self.m_states[key] = globals()[key](obj)

    def update(self):
        if ENUM_FSM_STATES[self.m_current] in self.m_states:
            self.m_states[ENUM_FSM_STATES[self.m_current]].update()

    def change_state(self, index, arg1=None):
        if index in self.m_fsm[ENUM_FSM_STATES[self.m_current]]:
            ret1 = self.m_states[ENUM_FSM_STATES[self.m_current]].end()
            self.m_last_state = self.m_current
            self.m_current = index
            self.m_states[ENUM_FSM_STATES[self.m_current]].begin(ret1 if not arg1 else arg1)
            return True
        return False

    def get_current_state(self):
        return self.m_states[ENUM_FSM_STATES[self.m_current]]
