import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance={i:float("inf") for i in range(1,n+1)}
     
        distance[k]=0
        d={}
        for p,q,r in times:
            if p not in d:
                d[p]=[]
            d[p].append((q,r))
      
        h = [(0,k)]
        while h:
            dist,node=heapq.heappop(h)

            if dist>distance[node]:
                continue
            
            for neighbour,weight in d.get(node,[]):
                new_dist=dist+weight
                if new_dist < distance[neighbour]:
                    distance[neighbour]=new_dist
                    heapq.heappush(h,(new_dist,neighbour))

        ans=max(distance.values())
        if ans==float("inf"):
            return -1
        return ans