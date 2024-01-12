from codes.JsonManager import JsonManager
from codes.FSM.Idle import Idle
from codes.FSM.Move import Move
from codes.FSM.Attack import Attack
from codes.FSM.Injured import Injured
from codes.FSM.Dead import Dead

ENUM_FSM_STATES = ["Idle", "Move", "Attack", "Injured", "Dead"]


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

    def change_status(self, index):
        if index in self.m_fsm[ENUM_FSM_STATES[self.m_current]] and index != ENUM_FSM_STATES[self.m_current]:
            self.m_states[ENUM_FSM_STATES[self.m_current]].end()
            self.m_last_state = self.m_current
            self.m_current = index
            self.m_states[ENUM_FSM_STATES[self.m_current]].begin()
            return True
        return False
