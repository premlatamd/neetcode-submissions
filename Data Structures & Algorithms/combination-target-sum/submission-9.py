class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        total=0
        arr=[]
        ans=[]

        def rev(level):
        
            nonlocal target
            nonlocal total
            nonlocal arr
            nonlocal nums
            nonlocal ans

        
            if target==total:
                if sorted(arr) not in ans:
                    ans.append(sorted(arr[:]))
                return
            if target < total:
                return
            
            if level>=len(nums):
                return 
            
            
            for i in range(level,len(nums)):
                total+=nums[i]
                arr.append(nums[i])
                rev(i)
                
                m=arr.pop()
                total-=m
                
                
            
            return ans

        return rev(0)
        """ans=[]
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
                total=0
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
        """