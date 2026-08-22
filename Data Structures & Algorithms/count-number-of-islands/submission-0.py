ADJACENT_INDICES = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited_grid = [[False] * len(grid[0]) for _ in range(len(grid))]
        islands = 0
        stack = []
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                
                if visited_grid[j][i]:
                    continue

                visited_grid[j][i] = True

                if grid[j][i] == '1':
                    stack.append([i, j])
                    islands += 1

                while stack:
                    x, y = stack.pop()
                    visited_grid[y][x] = True
                    if grid[y][x] == '0':
                        continue

                    for dx, dy in ADJACENT_INDICES:
                        if x+dx < 0 or x+dx >= len(grid[0]) or y+dy < 0 or y+dy >= len(grid):
                            continue
                        if visited_grid[y+dy][x+dx]:
                            continue
                        stack.append([x+dx, y+dy])
        return islands
