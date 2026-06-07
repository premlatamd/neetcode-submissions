from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[]
        s=0
        for i in range(len(nums)):
            pre=nums[:i]
            suf=nums[i+1:]
            s=prod(pre)*prod(suf)
            a.append(s)

        return a