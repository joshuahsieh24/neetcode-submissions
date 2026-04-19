class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0 #max profit
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy) #current price - minimum buy price
            minBuy = min(minBuy, sell)
        return maxP
        