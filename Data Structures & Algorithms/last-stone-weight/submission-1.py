import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [s * -1 for s in stones]
        heapq.heapify(stones_heap)
        while len(stones_heap) > 1:
            a, b = heapq.heappop(stones_heap) * -1, heapq.heappop(stones_heap) * -1

            if a == b:
                continue
            heapq.heappush(stones_heap, abs(a - b) * -1)
            
        return stones_heap[0] * -1 if stones_heap else 0