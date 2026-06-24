class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a=[]
        for i in range(len(matrix)):
            a.extend(matrix[i])

        print(a)

        l=0
        h=len(a)-1

        """if l>h:
            return False"""
        
        while l<=h:
            if l==h and target == a[l]:
                return True
            mid=((l+h)//2)
            if a[mid] < target:
                l=mid+1
            elif a[mid] > target:
                h=mid-1
            elif a[mid] == target:
                return True
            

        return False
        