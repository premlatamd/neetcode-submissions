from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s="balloon"
        s1=Counter(s)
        arr=[]
        set1=set()
        for i in text:
            if i in s:
                arr.append(i)
        a1=Counter(arr)
       
        print(a1,s1)
        for i in s1:
            if a1[i]>=s1[i]:
                r=a1[i]//s1[i]
                set1.add(r)
            else:
                return 0
        print(set1)
        if set1:
            return min(set1)
        if len(set1)==1:
            return list(set1)[0]
        
        return 0

        
