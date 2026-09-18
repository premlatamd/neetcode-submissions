class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            if i in nums2:
                index=nums2.index(i)
                for j in nums2[index+1:]:
                    if j > i:
                        ans.append(j)
                        break
                    
                else:
                    ans.append(-1)
            else:
                ans.append(-1)
        return ans

        
        