class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a=[]
        ans=[]
        i=n=len(temperatures)-1
        while i>=0:
           
            if a==[]:
                ans.append(0)
                a.append(temperatures[i])
            else:
                k=1
                for j in range(len(a)-1,-1,-1):
                    if a[j] > temperatures[i]:
                        index=k
                        ans.append(k)
                        k=1
                        break
                    k+=1
                else:  
                    ans.append(0)
                a.append(temperatures[i])
                    
                
            i-=1
        ans.reverse()

        return ans



        