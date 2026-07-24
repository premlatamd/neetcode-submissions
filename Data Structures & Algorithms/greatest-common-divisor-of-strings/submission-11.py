class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if len(str1)<len(str2):
            mini=str1
            maxi=str2
        else:
            mini=str2
            maxi=str1
        if mini not in maxi:
            return ""
        def check(maxi,mini):
            l=len(mini)
            i=1
            temp=mini
            while temp!="":
                if  i*temp==maxi:
                    print("hola",i*temp,maxi)
                    return temp
                
                if (i*temp) in maxi and len(i*temp)<=len(maxi):
                    if (i*temp)==maxi:
                        print("hello")
                        return temp
                    else:
                        i+=1
                        continue
                if (i*temp) not in maxi or len(temp)>len(maxi):
                    temp=mini[:l-1]
                    l-=1
                    i=1
                    continue
                i+=1
            return ""   
        ans=check(maxi,mini)
        f_ans=check(mini,ans)
        return f_ans 

        
        
            

        