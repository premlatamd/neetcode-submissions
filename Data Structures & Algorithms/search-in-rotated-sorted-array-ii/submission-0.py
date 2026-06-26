class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        a=[]
        m=nums[0]
        for i in range(len(nums)):
            if m > nums[i]:
                a.extend(nums[i:])
                nums=nums[:i+1]
                index=i
                break
        if a != [] and target <= a[-1]:
            #take a list
            for i in range(len(a)):
                if a[i]==target:
                    return True
        else:
            for i in range(len(nums)):
                if nums[i]==target:
                    return True
        return False