from collections import Counter
import heapq
class Solution:
    def maxDifference(self, s: str) -> int:
        freq=Counter(s)

        odd=[]
        even=[]
        print(freq)
        for i in freq.values():
            if i%2!=0:
                odd.append(i)
            else:
                even.append(i)
        
        a=max(odd)-min(even)
        return a
            
        

        