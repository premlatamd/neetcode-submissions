class Solution:
    def findMin(self, nums: List[int]) -> int:
        m=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<m:
                return nums[i]
        return m
            
        