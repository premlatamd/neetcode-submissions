class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""

        l=float("inf")
        ans=""

        
        n=len(s)
    
        for i in range(n):
            for j in range(i+1,n+1):
                p=s[i:j]
                
               
                for k in t:
                    if t.count(k)>p.count(k):
                        break
                else:
                    if len(p)<l:
                        l=len(p)
                        ans=p
                       
        return ans
                

                    
                
            
       