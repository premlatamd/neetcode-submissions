class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1

        l1=0
        l2=0
        n=len(nums)
        left=0
        right=1
        maxi=0
        
        while left<=n-1 and right <= n-1:
            while right<=n-1 and nums[left] < nums[right]:
                l1+=1
                left+=1
                right+=1

            while right<=n-1 and nums[left] > nums[right]:
                l2+=1
                left+=1
                right+=1

            while right<=n-1 and nums[left] == nums[right]:
                left+=1
                right+=1

            maxi=max(maxi,max(l1,l2))
            l1=l2=0
            
            

            if right== n-1:
                break
        return maxi+1
         