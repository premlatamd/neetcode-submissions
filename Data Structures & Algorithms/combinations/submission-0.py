class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr=[i for i in range(1,n+1)]
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


        