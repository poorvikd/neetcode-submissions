class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        n = len(prices)
        maxProfit = 0
        for i in range(1,n):
            profit = prices[i] - buy
            if profit < 0:
                buy = prices[i]
            else:
                maxProfit = max(maxProfit, profit)
        return maxProfit
            

