class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            # print(f"{l=} | {r=}")
            mid = (l + r) // 2
            days_to_ship = self.calculate_days_to_ship(weights, mid)
            if days_to_ship > days:
                l = mid + 1
            else:
                r = mid
        return l
    
    def calculate_days_to_ship(self, weights: List[int], max_weight: int) -> int:
        days = 0
        current_weight = 0
        for w in weights:
            if current_weight + w <= max_weight:
                current_weight += w
            else:
                days += 1
                current_weight = w
        return days + 1
        