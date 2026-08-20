import heapq

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def origin_distance(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def __lt__(self, other) -> bool:
        return self.origin_distance() < other.origin_distance()
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_heap = [Point(p[0], p[1]) for p in points]
        heapq.heapify(points_heap)

        # print(f"{[p for p in points_heap]}")

        results = []
        for _ in range(k):
            p = heapq.heappop(points_heap)
            results.append([p.x, p.y])
        return results