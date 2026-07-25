class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        s1=set(i for i in s)
        s2=set(i for i in t)
        print(s1,s2)
        if len(s1)!=len(s2):
            return False

        for i,j in zip(s,t):
            if i not in d:
                d[i]=set()
            d[i].add(j)
            if len(d[i])>1:
                return False
        return True
            
        