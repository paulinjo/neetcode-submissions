ADJACENT = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        height, width = len(board), len(board[0])
        
        visited = [[False] * width for _ in range(height)]
        is_edge = lambda x, y : x == 0 or y == 0 or x == (width - 1) or y == (height - 1)

        stack = []
        for j in range(height):
            for i in range(width):
                if visited[j][i]:
                    continue

                if board[j][i] == "X":
                    continue

                stack.append((i, j))
                path = []
                while stack:
                    x, y = stack.pop()
                    visited[y][x] = True
                    path.append((x, y))

                    for dx, dy in ADJACENT:
                        new_x, new_y = x+dx, y+dy

                        if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
                            continue

                        if board[new_y][new_x] == "X":
                            continue

                        if visited[new_y][new_x]:
                            continue

                        stack.append((new_x, new_y))
                
                if not any(is_edge(x, y) for x, y in path):
                    for x, y in path:
                        board[y][x] = "X"

