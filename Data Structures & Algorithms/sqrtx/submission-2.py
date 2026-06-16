import math as m
class Solution:
    def mySqrt(self, x: int) -> int:
        mul=1
        i=1
        if x==0:
            return 0
        while mul<=x :
            mul=i*i
            if mul==x:
                return i
            i+=1
        
        if mul>x:
            return (i-2)        
        #return int(m.sqrt(x))