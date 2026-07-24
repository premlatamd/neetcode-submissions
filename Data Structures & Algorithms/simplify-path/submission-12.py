class Solution:
    def simplifyPath(self, path: str) -> str:
        
        """path=path.lstrip("/.")
        path=path.rstrip("/")"""
        s=[]
        l=0
        h=path.split("/")
        print(h)
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


            

           



        """s=[]
        for key,i in enumerate(path):
           
            if (i=="/" and temp[-1]=="/") or i==".":
                s.append(i)
                continue
            
            temp+=i

        
        a=""
        if s:
            a+=s.pop()
        if s:
            a+=s.pop()

        if a=="..":
            return temp[:len(temp)-3]
        

        return temp"""
       



        