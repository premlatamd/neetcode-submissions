class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d={}
        for i in words:
            for j in i:
                if j not in d:
                    d[j]=0
                d[j]+=1
        for value in d.values():
            if value%len(words)!=0:
                return False
        return True

        
        