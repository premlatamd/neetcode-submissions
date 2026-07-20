class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        d={}
        for i in range(26):
            d[i+1]=chr(65+i)
        if columnNumber <= 26 :
            return d[columnNumber]
        s=[]
        q=columnNumber
       
        while q > 26:
            r=q%26
            q=q//26
            s.append(d[r])
           
        s.append(d[q])
        print(s)
        ans="".join(s[::-1])
        return ans

            


        
        