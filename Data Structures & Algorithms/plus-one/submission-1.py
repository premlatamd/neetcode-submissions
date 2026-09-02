class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def encode(arr):
            i=0
            total=0
            while arr!=[]:
                m=arr.pop()
                total+=m*(10**i)
                i+=1

            return total
        
        def decode(number):
            n=number
            ans=[]
            while n!=0:
                r=n%10
                n=n//10
                ans.append(r)
            ans.reverse()
            return ans
        
        result=encode(digits)
        ans=decode(result+1)

        return ans