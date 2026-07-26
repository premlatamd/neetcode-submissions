from  collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        count=2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))

        while q:
            row,col=q.popleft()
            #grid[row][col]=3
            count=grid[row][col]
            for r,c in [(-1,0),(0,-1),(0,1),(1,0)]:
                new_r=r+row
                new_c=c+col

                if new_c<0 or new_r<0 or new_c>=len(grid[0]) or new_r>=len(grid):
                    continue

                if grid[new_r][new_c]==0 or grid[new_r][new_c]>=3 or grid[new_r][new_c]==2:
                    continue

                grid[new_r][new_c]=count+1
                q.append((new_r,new_c))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
            
        ans=count-2
        return ans
            

                



        