from collections import deque
import math

EMPTY, FRESH, ROTTEN = 0, 1, 2
ADJACENT = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        stack = deque()

        minutes_grid = [[math.inf] * width for _ in range(height)]

        for y in range(height):
            for x in range(width):
                if grid[y][x] == ROTTEN:
                    minutes_grid[y][x] = 0
                    stack.append((x, y, 0))
        
        while stack:
            x, y, t = stack.popleft()
            
            for dx, dy in ADJACENT:
                new_x, new_y, new_t = x+dx, y+dy, t+1

                if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
                    continue

                if grid[new_y][new_x] != FRESH:
                    continue

                grid[new_y][new_x] = ROTTEN
                minutes_grid[new_y][new_x] = new_t
                stack.append((new_x, new_y, new_t))

        max_time = 0
        # print(f"{grid=} | {minutes_grid=}")
        for y in range(height):
            for x in range(width):
                if grid[y][x] == FRESH:
                    return -1
                if grid[y][x] == ROTTEN:
                    max_time = max(max_time, minutes_grid[y][x])
        return max_time