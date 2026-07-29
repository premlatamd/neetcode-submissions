from collections import Counter
class Solution:
    def maxScore(self, s: str) -> int:
        total=0
        for i in range(len(s)-1):
            left=list(s[:i+1])
            right=list(s[i+1:])
            
            sumi=left.count("0")+ right.count("1")
            if sumi>total:
                total=sumi

        return total



        