from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """a=[]
        s=0
        for i in range(len(nums)):
            pre=nums[:i]
            suf=nums[i+1:]
            s=prod(pre)*prod(suf)
            a.append(s)

        return a"""
        n = len(nums)
        ans = [1] * n

        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
            print(ans[i])

        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
            print(ans[i])

        return ans