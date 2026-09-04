from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g=defaultdict(list)
        ans=[]
        for n,w in zip(equations,values):
            u,v=n
            g[u].append((v,w))
            g[v].append((u,1.0/w))
        
        def dfs(g,visited,s,d):
            
            if s == d:
                return 1.0
            visited.add(s)

            for nei, w in g[s]:
                if nei in visited:
                    continue

                ans=dfs(g,visited,nei,d)
                if ans!=-1:
                    return w * ans

            return -1






            

        for s,d in queries:

            if s not in g or d not in g:
                ans.append(-1.00000)

            elif s==d:
                ans.append(1.00000)


            else:
                ans.append(dfs(g,set(),s,d))

        return ans
            
            
            

        """ g={}
        ans=[]
        for n,w in zip(equations,values):
            u,v=n
            g[u]=(v,w)
            g[v]=(u,1/w)
     
        

        for u,t in queries:
            if [t,u] in equations:
                v,wei=g[t]
                ans.append(1.0/wei)
                continue
            
        
            if u not in g:
                ans.append(-1.00000)
                continue

            v,wei=g[u]
            
        
            if t==v:
                ans.append(wei)

            elif t==u:
                ans.append(1.00000)

            elif u not in g.keys() or t not in g.keys():
                ans.append(-1.00000)

            else:
                visited=set()
                total=1.0
                while u not in visited and u!=t:
                    visited.add(u)
                    

                    try:
                        v,w=g[u]
                        u=v

                        total*=w

                    except:
                        total=-1.00000
                        break

                if u!=t:
                    ans.append(-1.00000)
                else:
                    ans.append(total)
            
        return ans
                        






        """