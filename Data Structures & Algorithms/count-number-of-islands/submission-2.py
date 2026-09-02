ADJACENT = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        height, width = len(grid), len(grid[0])
        results = 0
        
        def dfs(x: int, y: int):
            if grid[y][x] == "0":
                return

            grid[y][x] = "0"

            for dx, dy in ADJACENT:
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= width or ny < 0 or ny >= height:
                    continue

                if grid[ny][nx] == '0':
                    continue

                dfs(nx, ny)
        
        for y in range(height):
            for x in range(width):
                if grid[y][x] == "1":
                    results += 1
                    dfs(x, y)
        return results