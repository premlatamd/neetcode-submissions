from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        ans = []

        for i in range(len(nums)):

            # window ke bahar wale indices hatao
            while dq and dq[0] <= i - k:
                dq.popleft()

            # chhote elements hatao
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # pehli valid window ke baad answer add karo
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans



        """arr=[]
        i=0
        j=k
        while j<=len(nums):
            
            maxi=max(nums[i:j])
            arr.append(maxi)
            i+=1
            j+=1
        return arr"""


        