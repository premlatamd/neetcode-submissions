class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)==1:
            return 1
        
        left = 0
        right = 1
        
        l1 = 0
        ans = 1
        prev = -1
        
        while right < len(arr):
            
            if arr[left] < arr[right]:
                curr = 0
            elif arr[left] > arr[right]:
                curr = 1
            else:
                curr = 2
            
            if curr == 2:
                l1 = right
                prev = -1
            
            elif curr == prev:
                l1 = right - 1
                prev = curr
            
            else:
                ans = max(ans, right-l1+1)
                prev = curr
            
            left += 1
            right += 1
        
        return ans