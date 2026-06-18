
from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n= len(s1)
        
        k=0

        for l in range(k+len(s1),len(s2)+1):
            s=[]
            for j in s2[k:l]:
               
                if s2[k:l].count(j)!=s1.count(j):
                    break
                s.append(j)
            print(s) 
            if len(s)==len(s1):
                return True
        
            k+=1  
        
        return False

                


        
        