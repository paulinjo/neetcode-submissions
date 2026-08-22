from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

ADJACENT_INDICES = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        permimeter = 0
        island, visited = set(), set()
        
        def dfs(point: Point):
            nonlocal visited
            nonlocal island

            if point.y < 0 or point.y >= len(grid) or point.x < 0 or point.x >= len(grid[0]):
                return

            if grid[point.y][point.x]:
                island.add(point)

            visited.add(point)

            for dx, dy in ADJACENT_INDICES:
                new_point = Point(point.x + dx, point.y + dy)
                if new_point not in visited:
                    dfs(new_point)
        start = None
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]:
                    start = Point(x, y)
        assert start
        dfs(start)

        for point in island:
            adjacent_points = [Point(point.x + dx, point.y + dy) for (dx, dy) in ADJACENT_INDICES]
            permimeter += len([p for p in adjacent_points if p not in island])

        return permimeter
        