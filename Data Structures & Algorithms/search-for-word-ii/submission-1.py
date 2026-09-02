ADJACENT = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Node:
    def __init__(self, val: Optional[str] = None) -> None:
        self.val = val
        self.is_terminal = False
        self.word: Optional[str] = None
        self.children: dict[str, Node] = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        max_len = max([len(w) for w in words])
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = Node(c)
                node = node.children[c]
            node.is_terminal = True
            node.word = word
        
        results = set()
        def dfs(x: int, y: int, node: Optional[Node], path: set[tuple[int, int]]):
            nonlocal results
            if not node:
                return

            if node.is_terminal:
                results.add(node.word)
            
            if len(path) == max_len:
                return

            for dx, dy in ADJACENT:
                nx, ny = x+dx, y+dy
            
                if nx < 0 or nx >= len(board[0]) or ny < 0 or ny >= len(board):
                    continue

                if board[ny][nx] not in node.children:
                    continue

                if (nx, ny) in path:
                    continue

                dfs(nx, ny, node.children[board[ny][nx]], {*path, (nx, ny)})

        for y in range(len(board)):
            for x in range(len(board[0])):
                dfs(x, y, root.children.get(board[y][x]), {(x, y)})

        return list(results)

