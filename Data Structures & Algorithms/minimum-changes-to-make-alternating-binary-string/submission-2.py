class Solution:
    def minOperations(self, s: str) -> int:
        pattern=""
        for i in range(len(s)):
            if i%2==0:
                pattern+="1"
            else:
                pattern+="0"
        right=wrong=0
        for i,j in zip(s,pattern):
            if i==j:
                right+=1
            else:
                wrong+=1

        return min(right,wrong)


        print(pattern)
        """temp=s
        count=0
        if len(s)==1:
            return count
        if s[0]==s[1]:

        for i in range(len(s)-2):
            if  s[i]==s[i+1]:
                if s[i]=="0":
                    a="1"
                else:
                    a="0"
                s=s[:i+1]+a+s[i+2:]
                count+=1

        if s[-1]==s[-2]:
            if s[-2]=="0":
                s=s[:len(s)-1]+"1"
            else:
                s=s[:len(s)-1]+"0"
            count+=1

        return count"""
            

