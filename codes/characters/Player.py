import pygame
from codes import MyDefine
from codes.characters.Character import Character
from codes.EventTrigger import EventTrigger
from codes.EventTriggerManager import EventTriggerManager
from codes.Vector import Vector
from codes.BlockLayer import BlockLayer
from codes.PathFinding import PathFinding


class Player(Character, EventTrigger):

    def __init__(self):
        super().__init__()
        EventTriggerManager.get_instance().append_trigger(self)
        self.m_move_flag = False

    def update(self):
        super().update()

    def trigger(self, event):
        # Clicked on the right button
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_pos = pygame.mouse.get_pos()
            distance = (Vector(mouse_pos[0], mouse_pos[1]) - self.m_position).calculate_magnitude2()
            if distance <= (MyDefine.BLOCK_RESOLUTION[0] * 3) ** 2:
                self.m_path.clear()
                self.m_target_pos = Vector(mouse_pos[0], mouse_pos[1])
            else:
                blocks = BlockLayer.get_instance().m_blocks
                row = int(mouse_pos[1] // MyDefine.BLOCK_RESOLUTION[0])
                col = int(mouse_pos[0] // MyDefine.BLOCK_RESOLUTION[1])
                if blocks[row][col] != MyDefine.BLOCK_PLACEHOLDERS[0]:
                    direction = ((row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1),
                                 (row + 1, col - 1), (row + 1, col), (row + 1, col + 1))
                    for i in range(len(direction)):
                        if blocks[direction[i][0]][direction[i][1]] == MyDefine.BLOCK_PLACEHOLDERS[0]:
                            row = direction[i][0]
                            col = direction[i][1]
                            break
                self.m_path = PathFinding.astar_positions(blocks, (self.m_row, self.m_col), (row, col))
                self.m_path.append(Vector(mouse_pos[0], mouse_pos[1]))
            self.m_path_index = 0
            self.move()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.onDamaged(-self.m_max_hp * 20 / 100)
            elif event.key == pygame.K_a:
                self.attack(None)

            if event.key == pygame.K_UP:
                self.m_move_flag = True
                self.m_target_pos.z = self.m_position.z - 48
            if event.key == pygame.K_DOWN:
                self.m_move_flag = True
                self.m_target_pos.z = self.m_position.z + 48
            if event.key == pygame.K_LEFT:
                self.m_move_flag = True
                self.m_target_pos.x = self.m_position.x - 48
            if event.key == pygame.K_RIGHT:
                self.m_move_flag = True
                self.m_target_pos.x = self.m_position.x + 48

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.m_move_flag = False
                self.m_target_pos.z = self.m_position.z - 48
            if event.key == pygame.K_DOWN:
                self.m_move_flag = False
                self.m_target_pos.z = self.m_position.z + 48
            if event.key == pygame.K_LEFT:
                self.m_move_flag = False
                self.m_target_pos.x = self.m_position.x - 48
            if event.key == pygame.K_RIGHT:
                self.m_move_flag = False
                self.m_target_pos.x = self.m_position.x + 48
