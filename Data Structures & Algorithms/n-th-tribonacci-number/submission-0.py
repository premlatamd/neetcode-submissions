class Solution:
    def tribonacci(self, n: int) -> int:
        t0=0
        if n==0:
            return 0
        t1=1
        if n==1:
            return 1

        t2=1
        if n==2:
            return 1

       
        ans=t0+t1+t2
     
        for i in range(4,n+1):
            t0=t1
            t1=t2
            t2=ans
            ans=t0+t1+t2
        return ans
        