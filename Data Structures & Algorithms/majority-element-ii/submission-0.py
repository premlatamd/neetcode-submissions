class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        s=set(nums)
        n=len(nums)
        a=[]
        for i in s:
            if nums.count(i) > (n/3):
                a.append(i)
        return a

        