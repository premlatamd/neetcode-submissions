class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        mid=int((l+h)/2)
        while nums[mid]!=target:
            mid=int((l+h)/2)
            if l>=h:
                if target > nums[l]:
                    return l+1
                else:
                    return l
        
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                h=mid-1

        return mid
        

        