import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            k = (l + r) // 2
            hours_per_pile = [math.ceil(p / k) for p in piles]
            total_hours = sum(hours_per_pile)
            if total_hours > h:
                l = k + 1
            else:
                r = k - 1
        return l