class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr=[-1]*len(names)
        d={}
        for key,i in zip(names,heights):
            d[i]=key
        l=sorted(list(d.keys()),reverse=True)
        print(l)
        ans=[]
        for i in l:
            ans.append(d[i])
        print("hola",ans)
        return ans
        