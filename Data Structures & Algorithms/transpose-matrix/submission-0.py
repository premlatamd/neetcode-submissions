class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        t=[[0]*len(matrix) for i in range(len(matrix[0]))]
        print(t)
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                t[i][j]=matrix[j][i]
        return t

            
        