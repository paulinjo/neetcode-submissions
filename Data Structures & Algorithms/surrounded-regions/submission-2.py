ADJACENT = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        height, width = len(board), len(board[0])
        
        is_edge = lambda x, y : x == 0 or y == 0 or x == (width - 1) or y == (height - 1)

        stack = []
        for j in range(height):
            for i in range(width):
                if not is_edge(i, j):
                    continue

                if board[j][i] != "O":
                    continue

                stack.append((i, j))
                while stack:
                    x, y = stack.pop()
                    board[y][x] = "S"

                    for dx, dy in ADJACENT:
                        new_x, new_y = x+dx, y+dy

                        if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
                            continue

                        if board[new_y][new_x] != "O":
                            continue

                        stack.append((new_x, new_y))

        m = {
            "X": "X",
            "S": "O",
            "O": "X"
        }
        for j in range(height):
            for i in range(width):
                board[j][i] = m[board[j][i]]

