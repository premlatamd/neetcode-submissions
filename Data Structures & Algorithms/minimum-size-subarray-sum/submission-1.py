class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pre=0
        l=0
        m=float('inf')
        while l<=len(nums)-1:
            for r in range(l,len(nums)):
                pre+=nums[r]
                if pre>=target:
                    p=len(nums[l:r+1])
                    if m>=p:
                        m=p
                    break
            pre=0
            
            l+=1
        if m==float('inf'):
            return 0
        
        return m


            

    






        """for r in range(pre+1,len(nums)+1):
            s=nums[pre,r]
            suf=0
            sum=nums[pre]
            for i in s[suf+1:]:
                sum=sum+i+s[suf]
                if sum > target:
                    break
                if target== sum:
                    d.add(len(s))
                suf+=1
            pre+=1
"""

    
        