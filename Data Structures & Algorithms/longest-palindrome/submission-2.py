class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        c=0
        for i in s:
            if i not in d:
                d[i]=0
            d[i]+=1
        length=0
        for i in d.values():
            if i%2==0:
                length+=i
            else:
                if i>=3:
                    length+=(i-1)
                c=1
        if c:
            return length+1
        else:
            return length
            
        