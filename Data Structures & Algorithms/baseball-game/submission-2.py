class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a=[]
        n=len(operations)
        if n==0:
            return 0
        for i in operations:
        
            if i == "+":
                a1=a[len(a)-1]
                a2=a[len(a)-2]
                r=int(a1)+int(a2)
                a.append(str(r))

            elif i =="C":
                a.pop()
                print(a)
            elif i=="D":
                a3=int(a[len(a)-1])*2
                a.append(str(a3))
            else:
                a.append(i)
        print(a)
        sum=0
        for i in a:
            sum+=int(i)
        return sum