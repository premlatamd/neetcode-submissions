from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d=defaultdict(int)
        d1=defaultdict(int)
        for i in ransomNote:
            d[i]+=1

        for i in magazine:
            d1[i]+=1

        p=0
        for i in d:
            if i not in d1:
                return False

            if d[i]>d1[i]:
                return False

        return True

        