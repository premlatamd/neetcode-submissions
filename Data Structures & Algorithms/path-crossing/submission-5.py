class Solution:
    def isPathCrossing(self, path: str) -> bool:
     
        point=(0,0)
        s=set()
        s.add(point)
        for i in path:
            m,n=list(point)
            if i=="N":
               n=n+1
                
            elif i=="S":
                n=n-1
               
            elif i=="E":
                m=m+1

            elif i=="W":
                m=m-1

            point=(m,n)
            print(point)
            if point in s:
                return True
            else:
                s.add(point)

        return False
        
        
        