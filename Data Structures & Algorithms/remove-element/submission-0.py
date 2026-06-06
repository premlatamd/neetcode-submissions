class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        while n!=0:
            if nums[n-1] ==val:
                print(nums,nums[n-1])
                nums.remove(nums[n-1])
            
            n-=1

        return len(nums)
        