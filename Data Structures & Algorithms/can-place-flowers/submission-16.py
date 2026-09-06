class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        if flowerbed==[0] and n<=1:
            return True
        if flowerbed==[1]:
            return False

        l=len(flowerbed)

        for i in range(len(flowerbed)):
            if n==0:
                return True
            if flowerbed[i]==0 :
                if 0<=i-1<l:
                    if flowerbed[i-1]!=0:
                        continue
                    

                if 0<=i+1<l :
                    if flowerbed[i+1]!=0:
                        continue

                flowerbed[i]=1
                n-=1
        if n==0:
            return True
        return False
        
         
                

