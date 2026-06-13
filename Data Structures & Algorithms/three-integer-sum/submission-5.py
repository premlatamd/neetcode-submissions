

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        p=set()
        a=set()
        for i in range(0,n-1):
            s=set()
            for j in range(i+1,n):
                if (-(nums[i]+nums[j])) in s:
                    m=sorted([nums[i],nums[j],(-(nums[i]+nums[j]))])
                    a.add(tuple(m))            
                if nums[j] not in s:
                    s.add(nums[j]) 
            
        print(a)
        return [list(i) for i in a]



        """n = len(nums)

        s = set()

        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):

                    if nums[i] + nums[j] + nums[k] == 0:

                        p = tuple(sorted([nums[i], nums[j], nums[k]]))

                        s.add(p)

        return [list(x) for x in s]"""

        
        