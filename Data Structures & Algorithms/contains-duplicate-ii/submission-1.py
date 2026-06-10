class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d=set()
        c=0
        for i,j in enumerate(nums):
            if j in d:
                m=j
                c=1
                break
            d.add(j)

        if c==0:
            return False
        a=[]
        
        for i in range(0,len(nums)):
            if m==nums[i]:
                a.append(i)

        for i in range(0,len(a)-1):
            for j in range(i+1,len(a)):
                if abs(a[i]-a[j]) <= k:
                    return True
        return False
        