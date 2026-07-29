import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesHeap = [stone * -1 for stone in stones]
        heapq.heapify(stonesHeap)
        while len(stonesHeap) > 1:
            print(f"{stonesHeap=}")

            x = heapq.heappop(stonesHeap) * -1
            y = heapq.heappop(stonesHeap) * -1

            print(f"{x=}; {y=}")

            if x == y:
                continue
            else:
                heapq.heappush(stonesHeap, y - x)
        
        return stonesHeap[0] * -1 if stonesHeap else 0