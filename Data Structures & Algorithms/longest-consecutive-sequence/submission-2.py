class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        num=sorted(list(set(nums)))
        if len(num)==1:
            return len(num)
       
        for i in range(0,len(num)-1):
            n=num[i]

            for j in range(i+1,len(num)):
                if num[i] not in d:
                    d[num[i]]=[num[i]]
                m=num[j]
            
                if (m-n==1):
                    d[num[i]].append(m)
                    n=m
      
        l=0
        for key,i in d.items():        
            if l< len(i):
                l=len(i)
                b=i

        return l      
        