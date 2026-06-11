class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c={}
        

        
        l=0
        ans=0
        
        for r in range(len(s)):
            for i in range(26):
                c[chr(65+i)]=0
            ans=len(s[l:r+1])
           
            for i in s[l:r+1]:  
                c[i]+=1
            if ans-max(c.values())<=k:
                continue
            else:
                ans=ans-1
              
                l+=1
        return ans

            




        """a=[]
        m=0
        for i in range(len(s)):
            a.append(s[i])
            if m < a.count(s[i]):
                m=a.count(s[i])
                n=s[i]
                index=i

        pre=s[:index]
        suf=s[index+1:]
        print("hola",index)
        print("hola",suf)
        print("hola",pre)
        while k!=0:
            if pre[-1]!=n:
                pre=pre[:len(pre)-1]+n
                print(pre)
                k-=1
            else:
                suf=n+suf[1:]
                print(suf)
                k-=1
        print(pre+suf)
        return len(pre)+len(suf)




        """
        """for i in range(len(s)):
            if k==0:
                break
            if  s[i]!=n:
                print('hola',s[i])
                s=s[:i-1]+n+s[i+1:]  
                k-=1 
        print(s)
        p=0
        for i in range(0,len(s)-1):
            s1=""
            s1+=s[i]
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    s1+=s[j]
                else:
                    break

            if p < len(s1):
                p=len(s1)

        return p"""
