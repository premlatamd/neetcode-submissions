class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        t=""
        dp={}
        
        mini=len(s)

       

        def dfs(s):

            if s == "":
                return 0

            if s in dp and dp[s]!=-1:
                return dp[s]
            else:
                dp[s]=-1

            ans = len(s)

            for i in range(len(s)):

                left = s[:i+1]
                right = s[i+1:]

                if left in dictionary:
                    ans = min(ans, dfs(right))
                else:
                    ans = min(ans, len(left) + dfs(right))
            dp[s]=ans
            return ans
        return dfs(s)


        


  
                



       
        """ n=len(s)-1
        i=n
        count=0
        while len(t)<=n:
            if t in dictionary:
                
            t=s[]
            print(t)
            i-=1
            count+=1

        return count"""







        