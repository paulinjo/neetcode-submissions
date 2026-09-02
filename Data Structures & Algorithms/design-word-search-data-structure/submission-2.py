class Node:
    def __init__(self, val: Optional[str] = None) -> None:
        self.val = val
        self.children: dict[str, Node] = {}
        self.is_terminal = False

    def __repr__(self) -> str:
        return f"{self.val=} | {self.is_terminal=} | {self.children=}"
    

class WordDictionary:
    
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node(c)
            node = node.children[c]
        node.is_terminal = True

    def search(self, word: str) -> bool:
        stack = [(self.root, word)]
        while stack:
            node, remaining_letters = stack.pop()
            
            if not remaining_letters and node.is_terminal:
                return True

            if not remaining_letters and not node.is_terminal:
                continue

            next_letter = remaining_letters[0]
            if next_letter == ".": # wild card
                stack.extend([(child, remaining_letters[1:]) for child in node.children.values()])
                continue

            if next_letter not in node.children:
                continue

            stack.append((node.children[next_letter], remaining_letters[1:]))

        return False