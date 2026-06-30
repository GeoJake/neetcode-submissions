class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0
        
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):

                profit = prices[j] - prices[i]
                maxP = max(maxP, profit)
        
        return maxP