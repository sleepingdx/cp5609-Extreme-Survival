import heapq
from codes import MyDefine
from codes.Vector import Vector


class PathFinding:
    def __init__(self):
        pass

    @staticmethod
    def astar_array(grids, start, end):
        rows, cols = len(grids), len(grids[0])

        # the 4 possible target position/direction from current point. Thus, the reason why the eight directions are not
        # applicable is because the grid may be blocked, resulting in the character being blocked and unable to move.
        # directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 启发函数: Manhattan distance/Euclidean distance
        def heuristic(curr, goal):
            return abs(curr[0] - goal[0]) + abs(curr[1] - goal[1])

        # 堆的起始状态: (f, node, path)
        # f = g(起始节点到当前节点的实际代价) + h(当前节点到终点的启发值)
        # start - position of start point
        # path - the path from start point to current point
        heap = [(0, start, [])]
        # Refers to a collection that stores the coordinates of nodes that have been visited
        visited = set()

        while heap:
            # Corresponding to f, node and path
            cost, current, path = heapq.heappop(heap)
            # Already reached the end
            if current == end:
                return path + [current]
            # Pass the visited point
            if current in visited:
                continue
            visited.add(current)

            for direction in directions:
                # Possible next location
                new_pos = (current[0] + direction[0], current[1] + direction[1])

                # 神奇的Python, 还能这么写!!!
                if rows > new_pos[0] >= 0 == grids[new_pos[0]][new_pos[1]] and 0 <= new_pos[1] < cols:
                    new_cost = cost + 1 + heuristic(new_pos, end)
                    heapq.heappush(heap, (new_cost, new_pos, path + [current]))

        return []  # No path found

    @staticmethod
    def astar_positions(grids, start, end):
        path = PathFinding.astar_array(grids, start, end)
        positions = []
        for i in range(len(path)):
            positions.append(
                Vector(path[i][1] * MyDefine.BLOCK_RESOLUTION[0], path[i][0] * MyDefine.BLOCK_RESOLUTION[1]))
        return positions
