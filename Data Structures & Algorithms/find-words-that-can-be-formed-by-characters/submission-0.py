from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d1=Counter(chars)
        ans=final=0
        a=[]
        for i in words:
            d=Counter(i)
     
            b=1
            for j in d:
                if j in chars and d1[j]>=d[j]:
                    continue
                
                else:
                    b=0
                    break
                   
            if b:
                a.append(i)
        print(a)
        final=sum([len(i) for i in a])

        return final
            
            


        