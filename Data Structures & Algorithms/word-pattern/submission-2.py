from collections import deque,Counter
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
       
        

        l=s.split(" ")
        if len(pattern)!=len(l):
            return False
        
        d={}
        print(l)
        seti=set()
        for key,i in enumerate(pattern):
          
            if i not in d:
                d[i]=l[key]
                
            else:
                if d[i]!=l[key]:
                    return False
            seti.add(d[i])
        if len(seti)!=len(d):
            return False
           
        print(d)
        return True
        