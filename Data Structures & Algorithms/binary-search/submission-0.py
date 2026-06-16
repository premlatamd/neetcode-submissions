
class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        mid=int((l+h)/2)
        

        while nums[mid]!= target:
            if l>h:
                return -1
            mid=int((l+h)/2)
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                h=mid-1
        if nums[mid]==target:
            print(mid)
            return mid
        else:
            return -1
    


        