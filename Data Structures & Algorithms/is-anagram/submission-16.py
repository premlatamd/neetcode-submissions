
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        if len(s) != len(t):
            return False
        
        for ch in s:
            d[ch]=d.get(ch,0)+1
        for i in t:
            if i in d and d[i]>0:
                d[i]-=1
            else:
                return False
        return True


        """if len(s) != len(t):
            return False
        for i in s:
            if s.count(i)!=t.count(i):
                return False
        return True
        """
        

        """if len(s) != len(t):
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

        return t == """""