from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            d[i]=0
        for i in nums:
            d[i]+=1
            if d[i]>1:
                return True  
        return False
        """
        s=sorted(set(nums))
        nums=sorted(nums)
        if nums!=list(s):
            return True

        return False"""