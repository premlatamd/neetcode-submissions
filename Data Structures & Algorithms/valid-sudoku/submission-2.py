class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        c = [[1] * 9 for _ in range(9)]
        for i in board:
            pre=[]
            for j in i:
                if pre!=[] and j in pre and j!=".":
                    return False
                pre.append(j)
           
        for i in range(len(board)):
            for j in range(len(board)):
                c[i][j]=board[j][i]


        for i in c:
            suf=[]
            for j in i:
                if suf!=[] and j in suf and j!=".":
                    print("hellpa")
                    return False
                suf.append(j)

        
        for p in range(0,len(board),3):
            for q in range(0,len(board),3):
                b=[1]*9
                for i in range(p,p+3):
                    for j in range(q,q+3):
                        if board[i][j]!="." and board[i][j] in b:
                            print("hola")
                            return False
                        b.append(board[i][j])
        

        



        return True
           