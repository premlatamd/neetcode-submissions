from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        s=set()
        count=0
        d=Counter(arr)
        for i in d:
            if d[i]==1:
                count+=1
                if k==count:
                    return i

        return ""

