from collections import defaultdict, Counter
import json

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for s in strs:
            results[json.dumps(Counter(s), sort_keys=True)].append(s)
        
        return [v for v in results.values()]