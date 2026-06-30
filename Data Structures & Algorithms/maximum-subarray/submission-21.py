class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if nums==[]:
            return 0
        m=max(nums)
        if m<=0:
            return m
        left=0
        curr=0
        maxi=0
        for i in range(left,len(nums)):
            curr=max(nums[i],curr+nums[i])
            maxi=max(maxi,curr)
        return maxi
        """if len(nums)==1:
            return nums[0]
        if nums==[]:
            return 0
        m=max(nums)
        if m<=0:
            return m

        left=0
        right=left
        maxi=0
        sum=0
        while left <= len(nums)-1:
            while right<=len(nums)-1:
                sum+=nums[right]
                if sum >= maxi:
                    maxi=sum
                if sum<=0:
                    sum-=nums[left]
                    left+=1
                right+=1
            if right==len(nums):
                if sum>maxi:
                    sum=maxi
                if sum<=0:
                    sum-=nums[left]

            left+=1
        return maxi"""
        
        