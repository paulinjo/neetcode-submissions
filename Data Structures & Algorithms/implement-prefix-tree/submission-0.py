class Node:

    def __init__(self, val: str, end: bool = False) -> None:
        self.val = val
        self.end = end
        self.children: dict[str, Node] = {}


class PrefixTree:

    def __init__(self):
        self.trie: dict[str, Node] = {}

    def insert(self, word: str) -> None:
        current_level = self.trie
        for i, c in enumerate(word):
            is_end = i == len(word) - 1

            if c not in current_level:
                current_level[c] = Node(c, is_end)

            node = current_level[c]
            if is_end:
                node.end = True  # Ensure end flag is updated

            current_level = node.children  # Always move down

    def search(self, word: str) -> bool:
        current_level = self.trie
        node = None
        for c in word:
            if c not in current_level:
                return False
            node = current_level[c]
            current_level = node.children
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        current_level = self.trie
        node = None
        for c in prefix:
            if c not in current_level:
                return False
            node = current_level[c]
            current_level = node.children
        return node is not None