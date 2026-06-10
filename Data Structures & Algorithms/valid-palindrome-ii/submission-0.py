class Solution:
    def __init__(self):
        self.c=0
    def validPalindrome(self, s: str) -> bool:
        n=len(s)
        for i in range(0,n):
            if s[i]!=s[n-i-1]:
                if self.c==0:
                    self.c=1
                    if self.validPalindrome(s[(i):(n-i-1)]) or self.validPalindrome(s[(i+1):(n-i)]):
                        print(s[(i):(n-i-1)],s[(i+1):(n-i)])
                        return True
                return False
        return True
        