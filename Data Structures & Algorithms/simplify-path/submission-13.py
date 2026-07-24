class Solution:
    def simplifyPath(self, path: str) -> str:
    
        s=[]
        h=path.split("/")
        for key,i in enumerate(h):
            if i=="":
                continue
            if i==".":
                continue
                
            if i=="..":
                if s:
                    s.pop()
                    print(s)
                continue

            s.append(i)
    
        if s:
            ans="/"+"/".join(s)
        else:
            ans="/"
        
        return ans


            

     
       



        