import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d={}
        h=[]
        h1=deque()
        m=n
        for i in tasks:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
            
        for i in d:
            heapq.heappush(h,[-d[i],n+1])
        print(h)
              
        c=0
        while h or h1:
            c+=1
            for i in h1:
                i[1]=i[1]-1
            
            if h1 and h1[0][1]==0:
                    p,q=h1.popleft()
                    heapq.heappush(h,[p,n+1])
            if h:
                count,wait=heapq.heappop(h)
                count+=1
                if count!=0:
                    h1.append([count,n+1])

                
                    
                 
        
        print(c)
        return c
                

