import math as m
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def fun(n,r):
            m.factorial(n)/(m.factorial(n-r)*m.factorial(r))
        ans=[]
        for i in range(0,numRows):
            arr=[]
            for j in range(0,i+1):
                arr.append(int(m.factorial(i)/(m.factorial(i-j)*m.factorial(j))))
            ans.append(arr)
        return ans
        