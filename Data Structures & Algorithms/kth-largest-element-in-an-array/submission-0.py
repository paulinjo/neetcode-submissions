import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        
        result = 0
        for _ in range(k):
            result = heapq.heappop(max_heap)
        return -result