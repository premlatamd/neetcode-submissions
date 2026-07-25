class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        a=[]
        for key,i in enumerate(words):
            for key1,j in enumerate(words):
                if key!=key1 and i in j:
                    a.append(i)
                    break
        return a


        