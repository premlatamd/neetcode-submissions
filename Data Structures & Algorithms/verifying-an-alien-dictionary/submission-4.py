class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={}
        d1={}
        
        for i in range(26):
            d[i]=order[i]
            d1[order[i]]=i
        print(d1)
        n=len(words)
        for k in range(n-1):
            c=0
            for i,j in zip(words[k],words[k+1]):
                if d1[i]==d1[j]:
                    c=1
                    continue
                if d1[i]>d1[j]:
                    print("nklla")
                    return False
                if d1[i]<d1[j]:
                    c=0
                    break
            if c==1 and len(words[k])>len(words[k+1]):
                return False
        return True


            
        
                        

        """for i in words:
            for j in i:
                if j not in s:
                    s+=j
        m=sorted(s)
        print(m)

        temp=order[0:]
        for k in m:
            f=0
            for i ,j in enumerate(temp):
                if k==j:
                    temp=order[i+1:]
                    f=1
                    break
            if f==0:
                return False
        return True"""
        
        

        