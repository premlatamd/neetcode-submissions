class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m+n-i-1]=nums2[n-i-1]
        nums2=nums1
        for i in range(0,m+n):
            nums2[i]=Node(nums2[i])

        for i in range(0,m+n-1):
            for j in range(i+1,m+n):
                if nums2[i].data >= nums2[j].data:
                    nums2[i].data,nums2[j].data=nums2[j].data,nums2[i].data
                else:
                    continue
        for i in range(0,m+n-1):
            nums2[i].next=nums2[i+1]

        head=nums2[0]
        for i,j in enumerate(nums2):
            nums1[i]=j.data
        """ temp=head
        i=0
        while  i < m+n:
            
            temp=temp.next
"""


        

        
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        