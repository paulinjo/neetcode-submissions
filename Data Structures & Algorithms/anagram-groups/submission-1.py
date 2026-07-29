from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for s in strs:
            results[tuple(sorted(Counter(s).items()))].append(s)
        return [v for v in results.values()]