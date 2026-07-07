import math as m
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        a=1
        b=1
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return c
        
        """p=0
        n2=0
        ax=n
        f=0
        while n2<=ax:
            p=p+m.factorial(n)//(m.factorial(ax-n2)*m.factorial(f))
            print(m.factorial(n)//(m.factorial(ax-n2)*m.factorial(f)))
            n2+=2
            n-=1
            f+=1
        

        return p"""

        