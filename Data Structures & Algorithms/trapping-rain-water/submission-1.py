class Solution:
    def trap(self, height: List[int]) -> int:
        left=[]
        m=0
        for i in height:
            if m<=i:
                m=i
            left.append(m)

        right=[]
        n=0
        for i in range(len(height)-1,-1,-1):
            if n<=height[i]:
                n=height[i]
            right.append(n)

        right.reverse()
        print(left,right)
        area=0
        for j in range(len(height)):
            area+=min(left[j],right[j])-height[j]

        return area



    """   i=0
        pre=0
        suf=0
        ma=-1
        area=0

        while i<len(height)-1:
            if height[i]>0 and height[i] >= pre:
                pre=height[i]
            j=i+1
            k=0
            while j<len(height):
                suf=height[j]
                
                if pre!=0:
                    area+=k*min(pre,suf)

                   
                    if suf>=pre:
                        i=j
                        pre=height[j]
                        k=0
                        j+=1
                        continue
                    else:

                else: 
                    break
                k+=1
                j+=1

            i+=1

        return area"""
                


        