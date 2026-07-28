from collections import defaultdict
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        d=defaultdict(int)
        for i in allowed:
            d[i]+=1
        count=0
        for i in words:
            for j in i:
                if j not in d:
                    break
            else:
                count+=1
        return count


        