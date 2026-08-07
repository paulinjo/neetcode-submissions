class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {
            "[": "]",
            "{": "}",
            "(": ")",
        }

        stack = []
        for c in s:
            if c in valid_pairs:  # open brace
                stack.append(c)
                continue

            if not stack or valid_pairs.get(stack.pop()) != c:
                return False
        
        return not stack  # must be empty