from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_map = defaultdict(set)
        for a, b in trust:
            trust_map[a].add(b)

        for i in range(1, n+1):
            if i in trust_map:
                continue

            trusted = True
            for trustees in trust_map.values():
                if i not in trustees:
                    trusted = False
                    break
            if trusted:
                return i


        return -1