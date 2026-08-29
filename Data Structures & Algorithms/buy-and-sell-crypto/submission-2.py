class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        best = 0

        while l < r and r < len(prices):
            best = max(best, prices[r] - prices[l])

            if prices[r] < prices[l]:
                l += 1
            else:
                r += 1
            
            if l == r:
                r += 1
        return best