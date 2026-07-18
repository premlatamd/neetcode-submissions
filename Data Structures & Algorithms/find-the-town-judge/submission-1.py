class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        i=0
        ans=0
        d={}
        c=0
        while i<len(trust):
            if trust[i][1] not in d:
                d[trust[i][1]]=1
            else:
                d[trust[i][1]]+=1
            i+=1

        for i in d:
            if d[i]>ans:
                ans=d[i]
                key=i
                if ans==(n-1):
                    c=1
                    break
        for i in range(len(trust)):
            if trust[i][0]==key:
                c=0
                break
        if c==1:
            return key
        else:
            return -1





            
            