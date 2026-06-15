class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n=len(tokens)
        s=[]

        res=int(tokens[0])
        i=0
        while i<n:
            try:
                num=int(tokens[i])
                s.append(tokens[i])
            except:
                op1=s.pop()
                op2=s.pop()
                e=op2+tokens[i]+op1
                res=int(eval(e))
                s.append(str(res))
                print(res)
            i+=1
        print(res)
        return res
            

                