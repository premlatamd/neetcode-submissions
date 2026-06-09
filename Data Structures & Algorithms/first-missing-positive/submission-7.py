class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(nums)
        num=sorted(s)
        if num[0]-1 > 0 :
            return 1

        for i in range(0,len(num)-1):
            if (num[i]-num[i+1])==-1:
                continue
            elif num[i]+1 <= 0:
                m=num[i]+1
                while m <= 0 or m in num:
                    m=m+1
                return m

            else:
                return num[i]+1
        if (num[len(num)-1]+1) <= 0:
            return 1
        
        return num[len(num)-1]+1


            
        