ADJACENT_INDICES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        stack = []
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if not grid[j][i]:
                    continue
                
                current_area = 0
                stack.append([i, j])
                while stack:
                    # print(grid)
                    x, y = stack.pop()
                    if not grid[y][x]:
                        continue
                    
                    grid[y][x] = 0
                    current_area += 1

                    for dx, dy in ADJACENT_INDICES:
                        if x+dx < 0 or x+dx >= len(grid[0]) or y+dy < 0 or y+dy >= len(grid):
                            continue
                        stack.append([x+dx, y+dy])
                max_area = max(max_area, current_area)
        return max_area