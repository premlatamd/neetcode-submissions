class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k==len(arr):
            return arr
        a=[]
        h=len(arr)-1
        for j in range(k):
            d=float('inf')
            for i in arr:
               
                p=abs(i-x)
                if d > p:
                    d=p
                    m=i
            a.append(m)
            arr.remove(m)
        return sorted(a)
            
           
           
                

        
