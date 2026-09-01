class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        def find(x,parent):
            if parent[x]==x:
                return x
            parent[x]=find(parent[x],parent)
            return parent[x]

        def union(a,b,parent):
            pa=find(a,parent)
            pb=find(b,parent)
            if pa!=pb:
                parent[pb]= pa
                


        if len(edges)!=n-1:
            return False

        parent=[i for i in range(n)]
        visited=set()
        for u,v in edges:
            pu=find(u,parent)
            pv=find(v,parent)
            if pu==pv:
                return False
            else:
                if u<=v:
                    union(u,v,parent)
                else:
                    union(v,u,parent)
        return True
        



        