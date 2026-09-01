from collections import Counter
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[-1]*1000 for i in range(1000)]
        def lcs(s1,s2,i,j):

            if i>=len(s1) or j>=len(s2):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]

            if s1[i]==s2[j]:
                dp[i][j]=1+lcs(s1,s2,i+1,j+1)
                return dp[i][j]
            else:
                dp[i][j]=max(lcs(s1,s2,i+1,j),lcs(s1,s2,i,j+1))
                return dp[i][j]
        return lcs(text1,text2,0,0)

        


        