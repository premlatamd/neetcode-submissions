class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        head=Node(nums[0])
        temp=head
        a=[]
        for i in nums:
            if i not in a:
                a.append(i)
        
        for i in range(len(a)):
            nums[i]=a[i]

        return len(a)




        