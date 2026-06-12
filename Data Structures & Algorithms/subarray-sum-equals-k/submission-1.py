
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """n=len(nums)
        ans=[]
        c=0
        for i in range(1,n-1):
            if nums[i]==k:
                c+=1
        l=0
        pre=nums[0]
        r=0
        while l!=n :
            if pre== k:
                c+=1
            if r<n-1:
                r+=1
                pre=pre+nums[r]
                    
            else:
                pre=pre-nums[l]
                l+=1
        return c"""
      
        count = 0
        prefix_sum = 0
        freq = defaultdict(int)
        freq[0] = 1

        for num in nums:
            prefix_sum += num

            count += freq[prefix_sum - k]

            freq[prefix_sum] += 1

        return count
        


           

                 


        