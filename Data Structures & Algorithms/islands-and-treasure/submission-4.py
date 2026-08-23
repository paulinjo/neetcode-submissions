from collections import namedtuple, deque

Point = namedtuple('Point', ['x', 'y'])

WATER, TREASURE, INF = -1, 0, 2147483647
ADJACENT_INDICES = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        height, width = len(grid), len(grid[0])
        stack = deque()

        for y in range(height):
            for x in range(width):
                if grid[y][x] == TREASURE:
                    stack.append((Point(x, y), 0))

        while stack:
            point, distance = stack.popleft()
            
            for dx, dy in ADJACENT_INDICES:
                new_point = Point(point.x + dx, point.y + dy)
                new_distance = distance + 1

                if new_point.x < 0 or new_point.x >= width or new_point.y < 0 or new_point.y >= height:
                    continue
                
                if grid[new_point.y][new_point.x] == WATER:
                    continue

                if grid[new_point.y][new_point.x] != INF:  # previously found a better route
                    continue

                grid[new_point.y][new_point.x] = new_distance
                stack.append((new_point, new_distance))