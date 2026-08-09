from collections import deque
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        s=[]
        ans=[]
        def solve(i):
            nonlocal n
            nonlocal s
            nonlocal ans

            if n==i:
                ans.append(s[:])
                return 
                
            s.append(nums[i])
            solve(i+1)
            s.pop()
            solve(i+1)
            return ans
        return solve(0)





        """q=deque()
        i=0
        arr=[]
        q.append(arr)
        def loop(n,i,q):
            nonlocal nums
            if i>=n:
                return q
            l=len(q)
            for k in range(l):
                node=q.popleft()
                q.append(node)
                new_node=node[:]
                new_node.append(nums[i])
                q.append(new_node)
            return loop(n,i+1,q)

        return list(loop(len(nums),i,q))"""







        