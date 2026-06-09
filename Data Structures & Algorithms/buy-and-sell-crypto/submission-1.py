class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        n = len(prices)
        for i in range(1,n):
            profit = prices[i] - buy
            if profit < 0:
                buy = prices[i]
            else:
                maxProfit = max(profit,maxProfit)
        
        return maxProfit

            

