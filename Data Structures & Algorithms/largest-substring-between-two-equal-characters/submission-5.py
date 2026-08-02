class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d={}
        for i in range(len(s)-1):
            for j in s[i+1:]:
                if s[i] not in s[i+1:]:
                    break
                if s[i] not in d:
                    d[s[i]]=-1
                
                d[s[i]]+=1
                if s[i]==j:
                    break
        if d=={}:
            return -1
        return max(d.values())
           

    
        