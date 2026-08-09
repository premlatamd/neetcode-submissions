class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        s=[]
        total=0
        n=len(nums)
        def solve(i,total):
            nonlocal target
            nonlocal s
            nonlocal n
            nonlocal ans
            if target==total:
                ans.append(s[:])
                return
            if target<total:
                return

            if i>=n:
                return 
            total=total+nums[i]
            s.append(nums[i])
            solve(i,total)
            s.pop()
            total=total-nums[i]
            solve(i+1,total)
            return ans

        return solve(0,0)
        