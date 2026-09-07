class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m=t
        c=0
        for i in s:
            for k,j in enumerate(t):
                if i==j:
                    t=t[k+1:]
                    c+=1
                    break

        if c==len(s):
            return True
        return False

        