class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=s.lower().split(" ")
        p=''
        print(a)
        for i in a:
            for j in i:
                if j.isalnum():
                    p+=j

        print(p)
        n=len(p)
        for i in range(0,n):
            if p[i]!=p[n-1-i]:
                return False
        return True
        