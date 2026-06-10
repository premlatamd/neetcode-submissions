class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1=len(word1)
        n2=len(word2)
        n=min(n1,n2)
        word=""
        for i in range(0,n):
            word+=word1[i]+word2[i]
        word+=word1[n:]+word2[n:]
        return word        