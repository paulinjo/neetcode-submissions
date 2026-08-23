from collections import deque
from typing import List

ADJACENT = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        grid_height, grid_width = len(heights), len(heights[0])

        is_touching_pacific_ocean = lambda x, y: x == 0 or y == 0
        is_touching_atlantic_ocean = (
            lambda x, y: x == (grid_width - 1) or y == (grid_height - 1)
        )
        is_outside_grid = (
            lambda x, y: x < 0 or x >= grid_width or y < 0 or y >= grid_height
        )

        results = []

        # Fix 1: Corrected loop bound from grid_height to grid_width
        for j in range(grid_height):
            for i in range(grid_width):

                path = []
                stack = deque([(i, j)])
                visited = {(i, j)}  # Fix 2: Use a per-search visited set instead of modifying heights

                while stack:
                    x, y = stack.popleft()
                    path.append((x, y))

                    for dx, dy in ADJACENT:
                        new_x, new_y = x + dx, y + dy
                        if is_outside_grid(new_x, new_y):
                            continue
                        if (new_x, new_y) in visited:
                            continue

                        # Fix 3: Water flows downhill from current cell to neighboring cell
                        if heights[new_y][new_x] <= heights[y][x]:
                            visited.add((new_x, new_y))
                            stack.append((new_x, new_y))

                # Check if this starting cell can reach both oceans
                if any(
                    is_touching_atlantic_ocean(x, y) for x, y in path
                ) and any(is_touching_pacific_ocean(x, y) for x, y in path):
                    results.append([j, i])  # Output [row, col] format

        return results