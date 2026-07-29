class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        best = ""
        i = 0
        while True:
            current = None
            for s in strs:
                if i >= len(s):
                    return best
                current = current or s[i]
                # print(f"{current=}")
                if current != s[i]:
                    return best
            # print(f"{best=}; {i=}")
            best += s[i]
            i += 1
            