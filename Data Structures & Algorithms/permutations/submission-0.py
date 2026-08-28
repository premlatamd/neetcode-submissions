class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final=[]
        arr=[]
        def back():
            nonlocal arr
            nonlocal final
            if len(arr)==len(nums):
                if arr not in final:
                    final.append(arr[:])
                return 
            
            for i in nums:
                if i in arr:
                    continue
                arr.append(i)
                back()
                arr.pop()
        back()
        return final

