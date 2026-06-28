class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        for i in range(0,len(s)):
            a=""
            for j in range(i,len(s)):
                if s[j] not in a:
                    a+=s[j]
                else:
                    break
            if l < len(a):
                l=len(a)
        return l