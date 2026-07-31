from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        
        items = counter.items()
        return [i[0] for i in sorted(counter.items(), key=lambda i: i[1], reverse=True)[:k]]