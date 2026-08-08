from collections import deque
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        q=deque()
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

        return list(loop(len(nums),i,q))







        