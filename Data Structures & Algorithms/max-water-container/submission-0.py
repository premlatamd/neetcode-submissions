class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        m=0
        for k in range(len(heights)):
           
            if heights[i]<heights[j]:
                a=heights[i]*(j-i)
                i+=1
            else:
                a=heights[j]*(j-i)
                j-=1
            
            if m<a:
                m=a

        return m


        
        