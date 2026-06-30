class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i:int,j:int,grid: List[List[str]],visited:  List[List[str]]) -> None:
            q=deque()
            q.append((i,j))
            visited[i][j]=1
            while q:
                row,col=q.popleft()
                for xx,yy in [(-1,0),(0,-1),(0,1),(1,0)]:
                    
                    new_i=row+xx
                    new_j=col+yy
                    if new_i<0 or new_j<0 or  new_i>=len(grid) or new_j>=len(grid[0]):
                        continue

                    if grid[new_i][new_j]=="0":
                        continue

                    if visited[new_i][new_j]==1:
                        continue
                    visited[new_i][new_j]=1
                    q.append((new_i,new_j))
                
             



        count=0
        r=len(grid)
        c=len(grid[0])
        visited = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='1' and visited[i][j]==0:
                    bfs(i,j,grid,visited)
                    count+=1
        return count

        
        