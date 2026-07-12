class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        f = []

        while len(strs) != 0:

            base = strs[0]
            m = [base]

            j = 1

            while j < len(strs):

                o = strs[j]
                p = strs[j]

                found = 1

                if len(base) != len(o):
                    found = 0
                else:
                    for k in base:
                        c = 0

                        for key, l in enumerate(p):
                            if l == k:
                                p = p[:key] + p[key + 1:]
                                c = 1
                                break

                        if c == 0:
                            found = 0
                            break

                if found:
                    m.append(o)
                    strs.pop(j)   # matched word remove
                else:
                    j += 1

            strs.pop(0)   # base word remove
            f.append(m)

        return f
                        


                        

        