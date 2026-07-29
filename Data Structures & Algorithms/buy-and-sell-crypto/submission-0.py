class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        i, j = 0, 1
        while i <= j and j < len(prices):
            best = max(best, prices[j] - prices[i])

            if prices[j] < prices[i]:
                i = j
            
            j += 1
        return best
            