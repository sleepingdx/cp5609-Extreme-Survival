import heapq
from codes import MyDefine
from codes.Vector import Vector


class PathFinding:
    def __init__(self):
        pass

    def dijkstra(grid, start):
        rows, cols = len(grid), len(grid[0])
        distances = {(r, c): float('infinity') for r in range(rows) for c in range(cols)}
        distances[start] = 0

        heap = [(0, start)]

        while heap:
            current_distance, current_node = heapq.heappop(heap)

            row, col = current_node
            neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

            for neighbor in neighbors:
                r, c = neighbor
                if grid[r][c] == MyDefine.BLOCK_PLACEHOLDERS[0]:
                    if 0 <= r < rows and 0 <= c < cols:
                        new_distance = distances[current_node] + 1  # Assuming unweighted edges

                        if new_distance < distances[neighbor]:
                            distances[neighbor] = new_distance
                            heapq.heappush(heap, (new_distance, neighbor))

        return distances

    @staticmethod
    def dijkstra_ex(grid, pos):
        rows, cols = len(grid), len(grid[0])
        # Start position
        row_start = min(max(0, int(pos[1] // MyDefine.BLOCK_RESOLUTION[0])), rows - 1)
        col_start = min(max(0, int(pos[0] // MyDefine.BLOCK_RESOLUTION[1])), cols - 1)
        return PathFinding.dijkstra(grid, (row_start, col_start))

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
    def astar_pos(grids, start, end):
        path = PathFinding.astar_array(grids, start, end)
        positions = []
        for i in range(len(path)):
            positions.append(
                Vector(path[i][1] * MyDefine.BLOCK_RESOLUTION[0] + MyDefine.BLOCK_RESOLUTION[0] / 2,
                       path[i][0] * MyDefine.BLOCK_RESOLUTION[1] + MyDefine.BLOCK_RESOLUTION[1] / 2))
        return positions

    @staticmethod
    def astar_pos_ex(blocks, start_pos, end_pos, ignore_end=False):
        # Start position
        row_start = min(max(0, int(start_pos[1] // MyDefine.BLOCK_RESOLUTION[0])), len(blocks) - 1)
        col_start = min(max(0, int(start_pos[0] // MyDefine.BLOCK_RESOLUTION[1])), len(blocks[row_start]) - 1)
        # End position
        row_end = min(max(0, int(end_pos[1] // MyDefine.BLOCK_RESOLUTION[0])), len(blocks) - 1)
        col_end = min(max(0, int(end_pos[0] // MyDefine.BLOCK_RESOLUTION[1])), len(blocks[row_end]) - 1)
        # State
        state = blocks[row_end][col_end]
        if ignore_end:
            blocks[row_end][col_end] = 0
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
                        row_start = directions[i][0]
                        col_end = directions[i][1]
                        break
        path = PathFinding.astar_pos(blocks, (row_start, col_start), (row_end, col_end))
        if ignore_end:
            blocks[row_end][col_end] = state
        return path