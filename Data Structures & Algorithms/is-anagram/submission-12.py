class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        for i in s:
            c = 0

            for key, j in enumerate(t):
                if j == i:
                    t = t[:key] + t[key+1:]
                    c = 1
                    break

            if c == 0:
                return False

        return t == ""