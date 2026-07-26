from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    q.append((i,j))

        while q:
            row,col=q.popleft()
            
            count=grid[row][col]+1
            for r,c in [(1,0),(0,1),(0,-1),(-1,0)]:
                new_r=row+r
                new_c=col+c
                if new_r<0 or new_c<0 or new_r>=len(grid) or new_c>=len(grid[0]):
                    continue

                if grid[new_r][new_c]==-1 or grid[new_r][new_c]==-1 or grid[new_r][new_c]<=100:
                    continue

                grid[new_r][new_c]=count
                q.append((new_r,new_c))

            
                    

        