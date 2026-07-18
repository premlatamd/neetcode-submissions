class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans=0
        def check(r,c,grid,visited):
            visited[r][c]=1
            q=deque()
            q.append((r,c))
            count=1
            while q:
                row,col=q.popleft()
                for point in [(1,0),(0,1),(0,-1),(-1,0)]:
                    i,j=point
                    new_r=i+row
                    new_c=j+col
                    
                    if new_r<0 or new_c<0 or new_r>=len(grid) or new_c>=len(grid[0]):
                        continue

                    if visited[new_r][new_c]==1:
                        continue
                    if grid[new_r][new_c]==0:
                        continue
                    visited[new_r][new_c]=1
                    q.append((new_r,new_c))

                    count+=1
               
            return count


        visited=[[0]*len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and visited[i][j]==0:
                    area=check(i,j,grid,visited)
                    if ans<area:
                        ans=area

        return ans
    

        