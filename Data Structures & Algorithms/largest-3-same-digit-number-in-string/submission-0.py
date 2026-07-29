class Solution:
    def largestGoodInteger(self, num: str) -> str:
        a=[]
        for i in num:
            if i*3 in num:
                a.append(int(i))
        if a==[]:
            return ""
        return str(max(a))*3

        