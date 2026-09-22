
import math as m
class Solution:
    def reverse(self, x: int) -> int:

        if x==0:
            return 0
        m=2**31
        if -m>x or x>(m-1):
            return 0

        sign=""
        if str(x)[0]=='+':
            sign+='+'
        elif str(x)[0]=="-":
            sign+='-'
        
        n=abs(x)
        s=""
        while n>0:
            r=n%10
            n=n//10
            s+=str(r)
            print(s)
        if sign:
            s=sign+s

        if -m>int(s) or int(s)>(m-1):
            return 0

        return int(s)


        