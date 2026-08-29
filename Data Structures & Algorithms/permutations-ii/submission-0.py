class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        ans=[]
        s=set()
        A=nums
        def rev(level):
            if level==len(A):
                if arr not in ans:
                    ans.append(arr[:])
                return

            for i in range(len(A)):  
                if i in s:  
                    continue
                else:
                    s.add(i)
                    arr.append(A[i])
                    rev(level+1)
                    arr.pop()
                    s.remove(i)
            return ans

        return rev(0)
        