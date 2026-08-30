class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        s=""
        nums={'(':n,')':n}
        visited=set()

        
        

        def isValid(s):
            stack=[]
            for i in s:
                if i == '(':
                    stack.append(i)
                else:
                    if stack == []:
                        return False

                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        return False

            return True

        def rec():
            nonlocal nums,s,ans,n
            if len(s)==2*n:
                if isValid(s) and s not in ans:
                    ans.append(s)
                return

            for i in nums:
                
                if nums[i]==0:
                    continue

                nums[i]-=1
                s+=i
                rec()
                s=s[:-1]
                nums[i]+=1

            return ans

        return rec()
        
                
                


                

