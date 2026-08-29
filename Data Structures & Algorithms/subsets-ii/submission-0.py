class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        ans=[]

        def rec(index):
            nonlocal arr,ans,nums

            if index>=len(nums):
                m=sorted(arr[:])
                if m not in ans:
                    ans.append(m)
                return 

            #exclude
            rec(index+1)

            #include
            arr.append(nums[index])
            rec(index+1)
            arr.pop()
            return ans
        return rec(0)