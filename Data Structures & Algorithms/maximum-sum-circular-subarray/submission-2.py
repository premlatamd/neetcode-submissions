class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        temp=nums
        ans=temp[0]
        for i in range(len(nums)):
            sum=0
            maxi=temp[0]
            
            for j in range(len(nums)):
                sum+=temp[j]
                maxi=max(sum,maxi)
                if sum<0:
                    sum=0

            ans=max(ans,maxi)
            r=(i+1)%len(temp)
            
            if r!=0 or r!=len(nums)-1:
                temp=nums[r:]+nums[0:r]
    
        return ans