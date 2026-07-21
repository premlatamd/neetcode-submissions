import heapq as hp
import math as m
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for x,y in points:
            d=m.sqrt(x*x+y*y)
            hp.heappush(heap,[d,x,y])
        ans=[]
        for i in range(k):
            a,x,y=hp.heappop(heap)
            ans.append([x,y])

        return ans

        
        