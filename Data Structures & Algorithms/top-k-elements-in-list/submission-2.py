class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        p={}
        a=[]
        s=set(nums)

        m=0
        for i in s:
            p[i]=nums.count(i)
        print(p)
  
        for j in range(k):
            m=max(p.values())
            print(m)
            for i in p.keys():
                if p[i]==m and p[i]!=0:
                    a.append(i)
                    p[i]=0

            if len(a)==k:
                return a
        print(p)


          

        return a