
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited=set()
        ans=[]
        m=len(matrix)
        n=len(matrix[0])
        c=0
        r=0
        visited.add((0,0))
        ans.append(matrix[0][0])
        while len(visited)<(m*n):
            
            while c+1<n and (r,c+1) not in visited:
                print("1:",r,c+1)
                ans.append(matrix[r][c+1])
                visited.add((r,c+1))
                c+=1
            
            while r+1<m and (r+1,c) not in visited:
                print("2:",r+1,c)
                ans.append(matrix[r+1][c])
                visited.add((r+1,c))
                r+=1

            while c-1>=0 and (r,c-1) not in visited:
                print("3:",r,c-1)
                ans.append(matrix[r][c-1])
                visited.add((r,c-1))
                c-=1

            while r-1>=0 and (r-1,c) not in visited:
                print("4:",r-1,c)
                ans.append(matrix[r-1][c])
                visited.add((r-1,c))
                r-=1
        
        return ans





       