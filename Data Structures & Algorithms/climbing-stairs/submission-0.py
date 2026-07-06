import math as m
class Solution:
    def climbStairs(self, n: int) -> int:
        p=0
        n2=0
        ax=n
        f=0
        while n2<=ax:
            p=p+m.factorial(n)//(m.factorial(ax-n2)*m.factorial(f))
            print(m.factorial(n)//(m.factorial(ax-n2)*m.factorial(f)))
            n2+=2
            n-=1
            f+=1
        

        return p

        