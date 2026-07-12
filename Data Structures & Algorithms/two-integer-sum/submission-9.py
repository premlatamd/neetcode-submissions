class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            m=target-nums[i]
            if m not in d:
                d[nums[i]]=i
            else:
                return [d[m],i]
              
        

    

        """
        m=0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                m=nums[i]+nums[j]
                if m==target:
                    return [i,j]"""




