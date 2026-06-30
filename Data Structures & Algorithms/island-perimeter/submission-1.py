class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        peri=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    peri+=4
                    if i>0 and grid[i-1][j]==1:
                        peri-=1
                    if i<len(grid)-1 and grid[i+1][j]==1:
                        peri-=1

                    if j>0 and grid[i][j-1]==1:
                        peri-=1
                    if j<len(grid[0])-1 and grid[i][j+1]==1:
                        peri-=1

        return peri




