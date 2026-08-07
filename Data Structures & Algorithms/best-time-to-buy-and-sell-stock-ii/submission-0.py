class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        purchase_price = None
        for i in range(len(prices)):
            if purchase_price is None:
                if i == len(prices) - 1:
                    continue

                if prices[i] > prices[i+1]:
                    continue
                
                purchase_price = prices[i]
                print(f"bought for {purchase_price} on day {i}")
            else:
                if i == len(prices) - 1 or prices[i] > prices[i+1]:
                    print(f"sold for {prices[i]} on day {i}")
                    profit += prices[i] - purchase_price
                    purchase_price = None
        return profit