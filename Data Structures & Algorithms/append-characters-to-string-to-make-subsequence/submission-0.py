class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ans=0
        for key,i in enumerate(t):
            for k,j in enumerate(s):
                if i==j:
                    s=s[k+1:]
                    break
            else:
                ans=len(t[key:])
                break

        print(ans)
        return ans
            
