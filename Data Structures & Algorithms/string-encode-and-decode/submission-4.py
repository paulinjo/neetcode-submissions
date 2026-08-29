class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        print(f"{s=}")
        i, n = 0, 0
        results = []
        while i < len(s):
            if s[i] == "#":
                results.append(s[i+1:i+1+n])
                i += n+1
                n = 0
                continue
            n = n * 10 + int(s[i])
            i += 1
        return results