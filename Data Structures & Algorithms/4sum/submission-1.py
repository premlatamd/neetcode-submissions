class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums=sorted(nums)
       
        a=set()
        for i in range(0,n-2):
            for j in range(i+1,n-1):
                s=set()
                for k in range(j+1,n):
                    m=target-(nums[i]+nums[j]+nums[k])
                    if m in s:
                        a.add(tuple(sorted([nums[i],nums[j],nums[k],m])))

                    if nums[k] not in s:
                        s.add(nums[k])
                    
               
        return [list(i) for i in a]