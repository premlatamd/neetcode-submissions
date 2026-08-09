class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        s=[]
        ans=[]
        total=0
        n=len(candidates)
        candidates.sort()
        
        def solve(i,total):
            nonlocal n
            nonlocal ans
            nonlocal s
            nonlocal target
            if total==target and s[:] not in ans:
                ans.append(s[:])
                return
            if i>=n:
                return
            if total>target:
                return

            total=total+candidates[i]
            s.append(candidates[i])
            solve(i+1,total)
            s.pop()
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            total=total-candidates[i]
            solve(i+1,total)
            
            return ans
        ans=solve(0,0)
        

        return ans


        