class Solution:
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
        return p