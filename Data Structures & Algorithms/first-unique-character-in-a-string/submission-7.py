class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        visited=set()
        for i in range(len(s)):
            if s[i] in visited and s[i] in d:
                del d[s[i]]
            if s[i] not in d and s[i] not in visited:
                d[s[i]]=i
                visited.add(s[i])
           
        mini=float("inf")
        for key ,i in d.items():
            mini=min(mini,i)
       
        if mini!=float("inf"):
            return mini
        
        return -1

        
        