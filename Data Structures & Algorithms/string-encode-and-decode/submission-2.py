class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}|{s}"
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        l = ""
        i = 0
        while i < len(s):
            while s[i] != "|":
                l += s[i]
                i += 1
            i += 1
            size = int(l)
            result.append(s[i:i+size])
            i += size
            l = ""
        return result
