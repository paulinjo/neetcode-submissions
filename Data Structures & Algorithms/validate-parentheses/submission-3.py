class Solution:
    def isValid(self, s: str) -> bool:
        MATCHES = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        OPEN_PARENTHS = set("([{")

        stack = []
        for c in s:
            # print(f"{c=}")
            if c in OPEN_PARENTHS:
                # print(f"Appending {c=}")
                stack.append(c)
                continue

            if not stack:
                # print("No stack")
                return False

            last = stack.pop()
            # print(f"{last=}")
            if MATCHES.get(c) != last:
                return False
            
        return not stack

