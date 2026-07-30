from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(row,col,heights,count):
            visited=set()
            visited.add((row,col))
            q=deque()
            q.append((row,col))
            temp=set()
            while q:
                r,c=q.popleft()
                for x,y in [(0,1),(1,0),(0,-1),(-1,0)]:
                    new_r=r+x
                    new_c=c+y

                    if new_r>=len(heights) or new_c>=len(heights[0]):
                        temp.add("A")
                        continue

                    if new_r<0 or new_c<0:
                        temp.add("P")
                        continue

                    if heights[new_r][new_c]<=heights[r][c] and (new_r,new_c) not in visited:
                        q.append((new_r,new_c))
                        visited.add((new_r,new_c))

            if len(temp)==2 :
                count.append([row,col])
                        
            

            return count





        count=[]
       
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                count=bfs(i,j,heights,count)
        return count
                
