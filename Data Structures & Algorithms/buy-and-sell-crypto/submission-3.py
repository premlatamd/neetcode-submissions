"""class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        c=0
        for i in range(0,len(prices)-1):
            for j in range(i+1,len(prices)):
                if  prices[j]-prices[i] >= p:
                    c=1
                    p=prices[j]-prices[i]
        if c==0:
            return 0
        return p"""
class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit