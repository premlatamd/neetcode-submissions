class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=sorted(set(nums))
        nums=sorted(nums)
        print(list(s),nums)
        if nums!=list(s):
            return True

        return False