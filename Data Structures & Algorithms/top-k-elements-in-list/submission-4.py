class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Frequency Map
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Bucket Array
        bucket = [[] for _ in range(len(nums) + 1)]

        # Place each number in its frequency bucket
        for num, count in freq.items():
            bucket[count].append(num)

        # Step 3: Traverse from highest frequency
        ans = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans
        
            



        """ p={}
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


          

        return a"""