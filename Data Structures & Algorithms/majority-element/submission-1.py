from collections import Counter,defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        m=0
        for i in count:
            if count[i]>m:
                m=count[i]
                n=i
        print(n)

        return n      