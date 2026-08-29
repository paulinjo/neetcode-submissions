import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] -= 1
        
        count_items = [(count, n) for n, count in counts.items()]
        heapq.heapify(count_items)
        results = []
        for _ in range(k):
            results.append(heapq.heappop(count_items)[1])
        return results