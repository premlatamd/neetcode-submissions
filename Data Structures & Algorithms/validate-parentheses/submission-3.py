class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                a.append(i)
            elif i==')' and a!=[]:
                a1=a.pop()
                if a1 == '(':
                    continue
                else:
                    return False
            elif i=='}' and a!=[]:
                a1=a.pop()
                if a1 == '{':
                    continue
                else:
                    return False
            elif i==']' and a!=[]:
                a1=a.pop()
                if a1 == '[':
                    continue
                else:
                    return False
            else:
                return False
        if a==[]:
            return True
        return False
        

        