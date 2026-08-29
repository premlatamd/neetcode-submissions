class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=[i+1 for i in range(n)]
        arr=[]
        ans=[]
        def solve(level):
            nonlocal k
            nonlocal ans
            nonlocal arr
            nonlocal nums

            if level>=len(nums):
                l=len(arr[:])
                if k==l:
                    ans.append(arr[:])
                return
                
            solve(level+1)
            arr.append(nums[level])
            solve(level+1)
            arr.pop()
            return ans

        return solve(0)
        """arr=[i for i in range(1,n+1)]
        n=len(arr)
        s=[]
        ans=[]
        def solve(i):
            nonlocal n
            nonlocal s
            nonlocal ans

            if len(s[:])==k:
                ans.append(s[:])
                return 

            if i>=n:
                return

            s.append(arr[i])
            solve(i+1)
            s.pop()
            solve(i+1)

            return ans

        return solve(0)
"""

        